<br/>
<p align="center">
  <h3 align="center">Unlock the Curves: Mastering Polynomial Equations and R-squared Analysis</h3>

  <p align="center">
    Empower Your Data: Harness the Predictive Power of Polynomial Fits and Precision with R-squared Clarity!
    <br/>
    <br/>
  </p>
</p>



## Table Of Contents

* [About the Project](#about-the-project)
* [Built With](#built-with)
* [Getting Started](#getting-started)
* [Contributing](#contributing)
* [License](#license)
* [Authors](#authors)
* [Acknowledgements](#acknowledgements)

## About The Project

### Problem Scenario:

A team of environmental scientists is conducting a study on the daily temperature fluctuations in a particular region to understand its impact on local ecosystems. They have collected temperature readings at two-hour intervals from 6 AM to 7 PM on a specific day. The team needs to analyze this data to determine the temperature trend throughout the day and to identify any significant fluctuations that might affect the behavior and distribution of species in the area.

### Problem Requirements:
1. **Data Analysis**: Determine the average, median, and variability of the temperature readings.
2. **Data Completeness**: Ensure there are no missing readings to maintain the integrity of the analysis.
3. **Data Visualization**: Create a visual representation of the temperature readings across the time intervals.
4. **Temperature Extremes**: Identify the times with the highest and lowest temperatures, as these could be critical thresholds for species activity.
5. **Model Fitting**: Fit a model to the data to predict temperature trends and estimate temperatures at unmeasured times.
6. **Model Accuracy**: Calculate the accuracy of the fitted model to ensure its reliability.

### Solution Provided by the Code:

The Python script addresses the problem scenario as follows:

1. **Descriptive Statistics Calculation**: The script calculates and prints the mean, median, and standard deviation of the temperature readings, providing the team with an initial statistical understanding of the temperature data.

2. **Data Integrity Check**: It checks for missing values in both `Time` and `Temp` arrays, confirming the completeness of the data, which is crucial for accurate analysis.

3. **Initial Data Plotting**: A scatter plot is generated to visualize the observed temperature data across the time of day, offering an immediate visual understanding of temperature changes over time.

4. **Highlighting Temperature Extremes**: The script identifies the maximum and minimum temperature readings and highlights them on the plot. These points are crucial for understanding the temperature range that local species are experiencing.

5. **Polynomial Regression Model**: The script performs a polynomial regression with a degree of 2, providing a model (`p`) that fits the data points. This model allows the scientists to predict temperature trends and estimate temperatures at times that were not measured.

6. **Model Evaluation**: An R-squared value is computed and displayed, which quantifies how well the polynomial model explains the variation in the temperature data. A high R-squared value would indicate a good fit, thus a reliable model for the team's predictive needs.

7. **Final Visualization**: The script then displays the final plot with the observed data, the temperature extremes, the polynomial fit, and the model's equation and R-squared value. This comprehensive visualization aids the scientists in presenting their findings and making informed conclusions about temperature trends in the region.

By leveraging this script, the environmental scientists can efficiently analyze temperature data to aid in their ecological studies. The script's outputs provide both numerical and visual insights, facilitating a more profound understanding of how temperature variations could potentially affect the local ecosystem.

This Python script is designed to analyze and visualize a dataset containing two variables: Time and Temperature. It employs libraries such as NumPy, Matplotlib, and SciPy to accomplish this. 

1. **Importing Libraries**: 
   - `numpy` as `np` for numerical operations.
   - `matplotlib.pyplot` as `plt` for plotting graphs.
   - `scipy.stats` for statistical tools (though it's not directly used in the script).

2. **Data Initialization**: 
   - Two NumPy arrays, `Time` and `Temp`, are created to store the dataset. `Time` represents time points, and `Temp` represents corresponding temperature readings.

3. **Data Exploration**:
   - Descriptive statistics for the `Temp` array are calculated and printed, including mean, median, and standard deviation.
   - The script checks for any missing values (`NaN`) in both arrays.

4. **Initial Plotting**:
   - A plot is created showing the relationship between `Time` and `Temp`. Data points are marked as blue circles.
   - The plot is labeled with axes titles, a graph title, and a grid is added for better readability.

5. **Highlighting Extremes**:
   - The script identifies and highlights the maximum and minimum temperatures. This is done by finding the indices of these values in the `Temp` array and marking them on the plot in red and green, respectively.

6. **Polynomial Fit**:
   - A polynomial fit of degree 2 is computed for the data using `np.polyfit`. This function returns coefficients of the polynomial.
   - `np.poly1d` creates a polynomial function (`p`) from these coefficients.
   - This polynomial is plotted over the range of the `Time` data for visualization.

7. **Displaying the Polynomial Equation and R-squared**:
   - The polynomial equation is displayed on the plot. This equation represents the best-fit line through the data according to the least squares method.
   - The script calculates R-squared, a statistical measure of how close the data are to the fitted regression line. It's a proportion that indicates the percentage of the variance in the dependent variable (Temp) that's predictable from the independent variable (Time).

8. **Final Visualization**:
   - Finally, the script displays the plot with the observed data points, the polynomial fit line, and the annotations for the polynomial equation and R-squared value.

This script is useful for a basic analysis of how temperature varies with time, providing both a visual and statistical insight into the data. The inclusion of the polynomial fit and R-squared calculation allows for a more nuanced understanding of the data's trends and the fit's accuracy.

## Output Results 

### Descriptive Statistics:
- **Mean**: The average temperature across the measured times is approximately 8.64 degrees. This value is calculated by summing all temperature readings and dividing by the number of readings.
- **Median**: The middle value in the ordered list of temperatures is 9.0 degrees. This is the value separating the higher half from the lower half of the data sample.
- **Standard Deviation**: This is about 2.63 degrees, indicating the amount of variation or dispersion of the temperature values from the mean. A lower standard deviation would indicate that the data points tend to be closer to the mean.

The script also confirms that there are **no missing data points** in the datasets for time and temperature.

### Graphical Analysis:
- **Blue Dots (Observed Data)**: These represent the actual temperature measurements at different times.
- **Red Dot (Max Temp)**: Indicates the highest temperature recorded, which is approximately 12 degrees at 14:00 hours.
- **Green Dot (Min Temp)**: Indicates the lowest temperature recorded, which is approximately 4 degrees at 6:00 hours.
- **Blue Curve (2-Degree Polynomial Fit)**: This is the polynomial regression model fitted to the data. The curve shows the trend of temperatures over time based on a quadratic relationship. The curve peaks and then declines, suggesting temperatures rise to a point during the day and then fall.

### Polynomial Fit Equation:
The equation provided on the graph is:

\[ y = 0.1408x^2 + 3.821x - 14.26 \]

This equation represents the quadratic model that fits the observed temperature data, where \( y \) is the temperature and \( x \) is the time. The coefficients (0.1408, 3.821, -14.26) determine the shape and position of the parabola.

### R-squared:
The R-squared value is a statistical measure that represents the proportion of the variance for the dependent variable (temperature) that's explained by the independent variable (time) in the regression model. Here, an R-squared value of 0.966 suggests that approximately 96.6% of the variation in temperature can be explained by the time of day, indicating a very good fit of the model to the data.

### Exit Code:
The exit code 0 indicates that the script has finished running without any errors.

In summary, the output results indicate a well-fitting polynomial model that closely represents the variation of temperature over time with high accuracy, as evidenced by the high R-squared value. The descriptive statistics give a quick summary of the temperature data, and the plot visually represents these statistics along with the regression model.

## Built With

This section details the technologies and libraries used to build the Temperature Analysis project, which is showcased on GitHub. The project employs a mix of data analysis and visualization libraries in Python to study the relationship between time and temperature.

- **[NumPy](https://numpy.org/)** - A fundamental package for scientific computing in Python, NumPy provides support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays efficiently. It is used for storing and manipulating the dataset as well as for performing calculations of descriptive statistics.

- **[Matplotlib](https://matplotlib.org/)** - Matplotlib is a comprehensive library for creating static, interactive, and animated visualizations in Python. The project utilizes Matplotlib's `pyplot` module to plot the temperature data and the polynomial regression model, allowing for a visual exploration of the dataset's trends and patterns.

- **[SciPy](https://www.scipy.org/)** - While the `stats` module from SciPy is imported, it is not explicitly used in the provided code. However, SciPy is an open-source Python library used for scientific and technical computing, and it contains modules for optimization, linear algebra, integration, interpolation, special functions, FFT, signal and image processing, ODE solvers, and other tasks common in science and engineering.

The project's repository structure is as follows:

- `data_analysis.py`: The main Python script which contains all the data loading, processing, statistical analysis, and visualization code.

- `requirements.txt`: A file listing all the Python dependencies for the project, which can be installed using `pip install -r requirements.txt`.

- `README.md`: A Markdown file with an overview of the project, including the purpose, setup instructions, how to use the script, and a description of the Built With section.

- `LICENSE`: The license file that specifies the terms under which the project's source code can be used, modified, and distributed.

- `/images`: A directory containing the output plots generated by the script, showcasing the visual results of the analysis.

The project is designed to be a reusable template for temperature data analysis and could potentially be extended to include other types of time-series data analyses. The choice of these libraries ensures that the project has a solid foundation for numerical computation, data manipulation, and graphical representation.

## Getting Started

This section provides instructions on how to set up your local environment to run the Temperature Analysis project. This guide will take you through the steps of cloning the repository, installing the necessary dependencies, and running the script.

#### Prerequisites

Before you begin, ensure you have the following prerequisites installed on your system:
- Python 3.6 or higher
- pip (Python package installer)

#### Installation

1. **Clone the repository**
   
   Use the following command to clone the source code to your local machine:

   ```sh
   git clone https://github.com/your-username/temperature-analysis.git
   ```

   Replace `your-username` with your GitHub username or the username of the repository owner.

2. **Set up a virtual environment (Optional)**

   It's recommended to create a virtual environment to keep the dependencies required by the project separate from your global Python environment. Use the following commands:

   ```sh
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**

   Navigate to the cloned repository's directory and install the project dependencies using pip:

   ```sh
   cd temperature-analysis
   pip install -r requirements.txt
   ```

   This command will install NumPy, Matplotlib, and SciPy, which are required to run the script.

#### Running the script

Once you have installed all the necessary dependencies, you can run the script using:

```sh
python data_analysis.py
```

This will execute the code in `data_analysis.py`, which will output the descriptive statistics to the terminal and display the temperature versus time plot.

#### Plot Output

The script will generate a plot that visualizes the temperature data with respect to time, shows the maximum and minimum temperature points, and displays the fitted polynomial regression model. Ensure that you have a GUI environment capable of displaying the plot window.

#### Troubleshooting

- If you encounter any issues with the plot not displaying, ensure that your Matplotlib backend is configured correctly.
- If the script fails to run, double-check that you have activated your virtual environment and installed all the dependencies.

#### Contributing

If you would like to contribute to the project, please read the `CONTRIBUTING.md` file for guidelines on how to make pull requests, report bugs, and suggest enhancements.

This "Getting Started" section will help users to quickly set up and run the Temperature Analysis project locally. For detailed usage and further documentation, refer to the `README.md` file within the repository.

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.
* If you have suggestions for adding or removing projects, feel free to [open an issue](https://github.com/TribeOfJudahLion/Polynomial-Equation-and-R-Squared/issues/new) to discuss it, or directly create a pull request after you edit the *README.md* file with necessary changes.
* Please make sure you check your spelling and grammar.
* Create individual PR for each suggestion.
* Please also read through the [Code Of Conduct](https://github.com/TribeOfJudahLion/Polynomial-Equation-and-R-Squared/blob/main/CODE_OF_CONDUCT.md) before posting your first idea as well.

### Creating A Pull Request

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See [LICENSE](https://github.com/TribeOfJudahLion/Polynomial-Equation-and-R-Squared/blob/main/LICENSE.md) for more information.

## Authors

* **Robbie** - *PhD Computer Science Student* - [Robbie](https://github.com/TribeOfJudahLion/) - **

## Acknowledgements

* []()
* []()
* []()
