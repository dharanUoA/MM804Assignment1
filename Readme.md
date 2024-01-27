<a name="readme-top"></a>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-assignment">About The Assignment</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
  </ol>
</details>

<!-- ABOUT THE Assignment -->
## About The Assignment

The aim of this assignment is to create multiple view ports to compare different types of representation of objects, namely, wireframe, and surface with flat, Gouraud and Phong shading.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

* Python 3
* vtk 9.3.0

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

Download and install python 3 from [https://www.python.org/](https://www.python.org/).

### Installation

Install vtk packages
```sh
pip install vtk
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

### Run
```sh
python main.py
```
<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Configuration

Set ` output_to_image ` variable value.

- ` True `: for exporting the rendered scene as Image. The exported image will be stored in the root folder same as main.py named as ` output_image.jpg `. 
- ` False `: for interacting with the render scene.
