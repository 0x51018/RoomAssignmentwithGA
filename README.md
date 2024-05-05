**Dorm Room Assignment Using Genetic Algorithms**

Project Overview
- This project addresses the challenges faced by high school students assigned incompatible roommates in dormitory settings. By using surveys to collect preferences related to sleep time, sensitivity to noise, and preferred room temperature, we have developed an evaluation function to optimize room assignments based on lifestyle compatibility.

Technology Stack
- Language: Python
- Technique: Genetic Algorithm (GA)

How to Use
1. Clone this repository.
2. Place a student data file in CSV format in the parent directory of main. The data should include student names, preferred temperature, sleep time, and sensitivity to noise. Preferred sleep time and temperature should be divided into several categories, while sensitivity to noise is marked as 1 (sensitive) or 0 (not sensitive). Example data can be reviewed for reference.
3. Install the required Python libraries (e.g., numpy, pandas for data handling and manipulations).
4. Run the main script to execute the genetic algorithm, which iterates through generations to find the most compatible room assignments.
5. Check the output to review the optimized room assignment configurations.

Solution Approach
- Each potential room assignment configuration is represented as a "chromosome" in the genetic algorithm context. Genetic operations such as selection, crossover, and mutation are applied to evolve the population of room assignments towards an optimal setup. The fitness of each configuration is evaluated based on how well the student preferences are matched.

Development Status and Plans
- The initial algorithm was developed using mock data. We have since conducted studies with anonymized labeled data from the seventh cohort of students at the Sejong Academy of Science and Arts. Future developments will focus on refining the evaluation function, optimizing genetic operations, and adjusting the program to reflect factors considered by dormitory students at other schools to enhance satisfaction with room assignments. As of now, the code has not been updated since November 2022.

How to Contribute
- Contributions are welcome, especially from those with experience in genetic algorithms or educational administration. Please submit issues, fork the repository, or suggest enhancements through pull requests.
