#!/bin/bash

# Colors for better formatting
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Echo the Self Learning Project Template
echo -e "${GREEN}# Self Learning Project Template${NC}"
echo -e "${BLUE}## Goal : Fill the skills gaps by self learning while leveraging technology${NC}"
echo -e "\n${YELLOW}## Documentation for the Folder Structure${NC}"

# Create a formatted table for the folder structure
echo -e "| Section         | Description                                                                                                      | Action                |"
echo -e "|-----------------|------------------------------------------------------------------------------------------------------------------|-----------------------|"
echo -e "| **🌍 Real**         | *The Job That Starts with Objective and Key Results* - Sets goals and objectives, aligning tasks with measurable results. | Aim > Goals   |"
echo -e "| **🌳 Environments** | *The Roadmap and Use Cases* - A roadmap with learning modules and real-world use cases to apply new skills.            | Create > Runtimes |"
echo -e "| **🌌 Imaginary**    | *What You Learn on the Road* - Tracks concepts, theories, and skills acquired, promoting continuous growth.            | Capture > Screenshots |"
echo -e "| **📐 Formulas**     | *The Guides That Are Mentioned* - Essential guides and formulas for understanding and solving project challenges.     |  GPT > Learn from it |"
echo -e "| **🔣 Symbols**      | *Code That Is Implemented* - Includes code snippets and examples to demonstrate each concept practically.              |  Execute > Code   |"
echo -e "| **🌀 Semblance**    | *Errors Found in the Process* - Documents mistakes and solutions, making errors valuable learning opportunities.       |  Fix > Errors   |"

echo -e "\n${YELLOW}Practical Terminal Commands From Your Workstation${NC}"
echo -e "```bash"
echo -e "git pull; git add . ; git commit -m \"Codespaces\" -m \"updates\"; git push;sleep 3;clear"
echo -e "```"

echo -e "\n${YELLOW}Collaborators>${NC}"
echo -e "- Cheuk > https://www.linkedin.com/in/ch-c-797533177/"
echo -e "- Nawal > https://www.linkedin.com/in/nawalc/"
echo -e "- Tomi > https://www.linkedin.com/in/oluwatomi-amao-245b61189/"

echo -e "\n${YELLOW}prompts:${NC}"
echo -e "# 🎯 Objectives"
echo -e "- Develop a comprehensive self-learning framework that:"
echo -e "  - Maps learning stages to Lacan's triad concepts"
echo -e "  - Provides clear metrics for progress tracking"
echo -e "  - Includes practical validation methods"
echo -e "- Establish a systematic process to:"
echo -e "  - Identify current skill levels"
echo -e "  - Define target competencies" 
echo -e "  - Create actionable learning plans"
echo -e "  - Measure skill development"
echo -e "- Build a portfolio of real-world projects that:"
echo -e "  - Demonstrate applied knowledge"
echo -e "  - Solve actual business problems"
echo -e "  - Follow industry best practices"
echo -e "  - Include detailed documentation"

echo -e "\n# 📊 Key Results"
echo -e "- Implement folder structure mapping to Lacan's concepts"
echo -e "- Track progress through clear documentation and examples"
echo -e "- Validate learning through hands-on implementation"
echo -e "- Capture errors and solutions for continuous improvement"

echo -e "\n# 📝 Format Requirements"
echo -e "- Use clear markdown structure and headings"
echo -e "- Include relevant emojis for visual organization"
echo -e "- Add concise single-line comments for clarity"
echo -e "- Maintain consistent formatting throughout"
echo -e "- Eliminate redundant information"

echo -e "\n# ✅ Quality Checks"
echo -e "- Verify grammar and spelling"
echo -e "- Validate markdown syntax"
echo -e "- Ensure documentation completeness"
echo -e "- Test all code examples"
echo -e "- Review for duplicate content"

echo -e "\n${YELLOW}PromptFixer:${NC}"
echo -e "-act as a prompt engineer,review the prompt and ask your questions,write a better version of the prompt"

# Create directories for the structure if they don't exist
mkdir -p "🌍_Real" "🌳_Environments" "🌌_Imaginary" "📐_Formulas" "🔣_Symbols" "🌀_Semblance"

echo -e "\n${GREEN}Directories created successfully!${NC}"