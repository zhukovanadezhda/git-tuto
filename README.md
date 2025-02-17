# Collaborative Git Tutorial for Beginners

This repository is designed for **beginners** to practice **branching** and **pull requests** in a **practical session**. The file `calculate_area.py` contains **two deliberate mistakes** for you and a partner to discover and fix together, following a typical GitHub workflow.

---

## Task: Collaborate on a Project

1. **Pair Up**  
   Work with a partner to simulate real-world collaborative development.

2. **Fork the Repository (One Partner)**  
   - Click the **Fork** button at the top-right of this repository to create your own copy on GitHub.

3. **Clone the Repository (Both Partners)**  
   - Each partner should clone the **forked** repository to their local machine.

4. **Add Your Partner as a Collaborator (One Partner)**  
   - In your forked repository, go to **Settings → Collaborators** and add your partner’s GitHub username.

5. **Explore the Project**  
   - Review the files on your local machine. Focus on `calculate_area.py`.

6. **Run the Script**  
   - Open a terminal and run:
     ```
     python3 calculate_area.py
     ```
   - Observe the output and think about any unexpected behavior.

7. **Identify the Mistakes**  
   - Discuss with your partner to find the **two** intentional errors in `calculate_area.py`.  
   - Each person should fix **one** mistake—avoid changing anything else.

8. **Create a Branch**  
   - On your local machine, switch to a new branch to isolate your fix:
     ```
     git checkout -b fix-your-branch-name
     ```

9. **Commit Your Change**  
   - Stage and commit your fix with a clear, descriptive message:
     ```
     git add calculate_area.py
     git commit -m "Fix one of the issues in calculate_area.py"
     ```

10. **Push Your Branch**  
    - Send your changes to GitHub:
      ```
      git push -u origin fix-your-branch-name
      ```

11. **Create a Pull Request (PR)**  
    - On GitHub, open a PR from your branch to the `main` branch of your fork.  
    - Describe the change you made in the PR message.

12. **Review & Merge**  
    - Your partner reviews the PR. Once approved, merge it into `main`.

13. **Pull the Latest Changes**  
    - Update your local repository with:
      ```
      git checkout main
      git pull
      ```
    - Verify that the script behaves as expected.

By following these steps, you’ll gain hands-on experience with **branching**, **committing**, **creating pull requests**, and **merging**—essential skills for any collaborative GitHub project. Good luck, and have fun learning!

---

## Author

Nadezhda Zhukova  
[nadiajuckova@gmail.com](mailto:nadiajuckova@gmail.com)
