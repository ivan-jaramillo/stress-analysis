# Stress Analysis

Stress analysis at a point on a body.

## Description

When designing physical systems, it is important to account for the internal stresses generated by external forces. There are two kinds of stress that a body encounters - normal stress and shear stress. Average normal stress is the normal force acting over the cross-sectional area of a body. Average shear stress is the tangential force acting over the cross-sectional area of a body. For two-dimensional or three-dimensional problems, knowing the normal stress and shear stress on two or three orthogonal planes passing through a specific point allows us to know the stresses on any other section cut through that same specific point. This project looks at the stress at a point on a body from user-specified external forces or stress tensors.

## How to Install

Use a virtual environment! It's good developer practice and allows you to have installed certain versions of dependencies for your Python projects. This leads to less headaches and saves time.

You can make one by doing the following in your terminal:

```shell
python3 -m venv env
```

You can activate the virtual environment by doing the following:

```shell
source env/bin/activate
```

To install dependencies this project requires, you can do the following:

```shell
pip install -r requirements.txt
```

You can deactivate the virtual environment by doing the following:

```shell
deactivate
```

## How to Use

You can run this program while in your virtual environment by doing the following:

```shell
python stress_analysis/stress_analysis.py
```
