import time
import logging
from enum import Enum
from functools import wraps

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='circuit_breaker.log'
)
logger = logging.getLogger('circuit_breaker')

class CircuitState(Enum):
    CLOSED = 'CLOSED'  # Normal operation, requests pass through
    OPEN = 'OPEN'      # Circuit is broken, requests fail fast
    HALF_OPEN = 'HALF_OPEN'  # Testing if service is back to normal

class CircuitBreaker:
    def __init__(self, 
                 failure_threshold=5, 
                 recovery_timeout=10, 
                 fallback_function=None):
        """
        Initialize the circuit breaker.
        
        Args:
            failure_threshold: Number of failures before opening the circuit
            recovery_timeout: Time in seconds before attempting recovery
            fallback_function: Function to call when circuit is open
        """
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.fallback_function = fallback_function
        
        self.state = CircuitState.CLOSED
        self.failure_count = 0
        self.last_failure_time = None
        
        logger.info("🔌 Circuit Breaker initialized in CLOSED state")
    
    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return self._handle_call(func, *args, **kwargs)
        return wrapper
    
    def _handle_call(self, func, *args, **kwargs):
        if self.state == CircuitState.OPEN:
            if self._should_attempt_recovery():
                return self._try_half_open_call(func, *args, **kwargs)
            else:
                logger.warning("🚫 Circuit OPEN - Fast failing")
                return self._handle_open_circuit()
        
        elif self.state == CircuitState.HALF_OPEN:
            return self._try_half_open_call(func, *args, **kwargs)
        
        # Circuit is CLOSED, normal operation
        try:
            result = func(*args, **kwargs)
            # Successful call in HALF_OPEN state resets the circuit
            if self.state == CircuitState.HALF_OPEN:
                self._close_circuit()
            return result
        except Exception as e:
            return self._handle_failure(e)
    
    def _should_attempt_recovery(self):
        """Check if enough time has passed to try recovery"""
        if self.last_failure_time is None:
            return False
        
        elapsed = time.time() - self.last_failure_time
        return elapsed >= self.recovery_timeout
    
    def _try_half_open_call(self, func, *args, **kwargs):
        """Attempt a trial call in HALF_OPEN state"""
        logger.info("⚠️ Circuit HALF_OPEN - Testing service")
        self.state = CircuitState.HALF_OPEN
        try:
            result = func(*args, **kwargs)
            self._close_circuit()
            return result
        except Exception as e:
            self._open_circuit()
            return self._handle_open_circuit()
    
    def _handle_failure(self, exception):
        """Process a failure and potentially open the circuit"""
        self.failure_count += 1
        self.last_failure_time = time.time()
        
        logger.error(f"❌ Call failed: {str(exception)} (Failure count: {self.failure_count})")
        
        if self.failure_count >= self.failure_threshold:
            self._open_circuit()
            
        # Re-raise the exception if no fallback
        if self.fallback_function:
            return self.fallback_function(exception)
        else:
            raise exception
    
    def _open_circuit(self):
        """Open the circuit to prevent further calls"""
        if self.state != CircuitState.OPEN:
            logger.warning(f"🔓 Circuit OPENED after {self.failure_count} failures")
            self.state = CircuitState.OPEN
    
    def _close_circuit(self):
        """Close the circuit, returning to normal operation"""
        logger.info("🔒 Circuit CLOSED - Service recovered")
        self.state = CircuitState.CLOSED
        self.failure_count = 0
    
    def _handle_open_circuit(self):
        """Handle calls when circuit is open"""
        if self.fallback_function:
            return self.fallback_function(None)
        else:
            raise Exception("Circuit is OPEN - Service unavailable")
            
    def reset(self):
        """Manually reset the circuit to closed state"""
        logger.info("🔄 Circuit manually reset to CLOSED state")
        self.state = CircuitState.CLOSED
        self.failure_count = 0
        self.last_failure_time = None

```

```python
# cpu_load_generator.py

import os
import time
import random
import logging
import multiprocessing
from datetime import datetime
from circuit_breaker import CircuitBreaker

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='cpu_load.log'
)
logger = logging.getLogger('cpu_load')

def fallback_handler(exception):
    """Fallback function when circuit is open"""
    logger.warning("🔀 Using fallback function - returning cached/default result")
    return {
        "status": "degraded",
        "message": "Service is currently unavailable, using cached data",
        "timestamp": datetime.now().isoformat()
    }

# Apply circuit breaker to the CPU intensive function
@CircuitBreaker(failure_threshold=3, recovery_timeout=15, fallback_function=fallback_handler)
def cpu_intensive_task(complexity=1000000, fail_probability=0.3):
    """
    A CPU intensive function that might fail based on probability
    
    Args:
        complexity: Factor that influences CPU load
        fail_probability: Chance of failure (0-1)
    """
    start_time = time.time()
    process_id = os.getpid()
    
    logger.info(f"🏁 Starting CPU-intensive task on PID {process_id}")
    
    # Simulate CPU-intensive work
    result = 0
    for i in range(complexity):
        result += i * random.random()
        
        # Log progress periodically
        if i % (complexity // 10) == 0:
            logger.debug(f"⏳ Processing iteration {i}/{complexity}")
    
    # Simulate random failures based on probability
    if random.random() < fail_probability:
        logger.error("💥 Task is failing deliberately based on probability")
        raise Exception("Service overloaded or unavailable")
    
    execution_time = time.time() - start_time
    logger.info(f"✅ Task completed in {execution_time:.2f} seconds")
    
    return {
        "status": "success",
        "process_id": process_id,
        "execution_time": execution_time,
        "timestamp": datetime.now().isoformat()
    }

def run_parallel_tasks(num_processes=4, iterations=20):
    """Run multiple CPU-intensive processes in parallel"""
    print("🚀 Starting parallel CPU-intensive tasks with circuit breaker protection")
    print(f"📊 Using {num_processes} processes for {iterations} iterations each")
    
    for i in range(iterations):
        print(f"\n📌 Iteration {i+1}/{iterations}")
        
        # Increase failure probability as we progress to trigger circuit breaker
        fail_probability = min(0.1 + (i * 0.05), 0.9)
        
        try:
            # Adjust complexity to control CPU usage
            complexity = random.randint(500000, 2000000)
            result = cpu_intensive_task(complexity, fail_probability)
            print(f"🟢 Success: {result}")
        except Exception as e:
            print(f"🔴 Failed: {str(e)}")
        
        # Short delay between iterations
        time.sleep(1)

if __name__ == "__main__":
    print("🔄 CPU Load Generator with Circuit Breaker Pattern")
    print("🔍 Check 'cpu_load.log' and 'circuit_breaker.log' for detailed logs")
    
    # Run the demo
    run_parallel_tasks(num_processes=2, iterations=15)