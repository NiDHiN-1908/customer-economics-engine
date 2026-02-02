# Customer Economics Engine

**An Integrated Decision System for Churn-Driven CLV Optimization**

## Overview

Customer Economics Engine is an end-to-end decision support system designed to estimate **expected discounted profit per customer (Customer Lifetime Value)** and use it to **optimize marketing and retention strategies**. Unlike traditional CLV projects that focus only on prediction, this system treats CLV as a **business optimization problem**, where model outputs directly drive financial decisions.

The system integrates churn-based survival modeling with revenue and cost estimation to compute customer-level economic value under uncertainty. On top of this, a decision layer simulates alternative marketing strategies and evaluates them using profit and ROI metrics.

## System Inputs

The system expects the following core inputs:

* `customer_id` – Unique customer identifier
* `churn_probability` / survival curve – From churn model
* `monthly_revenue` – Customer revenue or ARPU
* `acquisition_cost` – Cost to acquire customer
* `retention_cost` – Cost to retain customer

## System Outputs

For each customer, the system produces:

* `CLV` – Expected discounted profit
* `recommended_action` – Invest / Ignore
* `expected_profit` – Monetary value under strategy

## Architecture

Data flows through the following pipeline:

Data → Survival Model → Revenue & Cost Model → CLV Engine → Decision Engine → Dashboard

All core logic is implemented as modular Python components inside the `src/` directory. The system is exposed through an interactive dashboard for real-time decision making.

## Key Features

* Churn-driven survival modeling
* Profit-aware CLV estimation
* Budget and ROI simulation
* Risk-aware customer segmentation
* Interactive decision dashboard

## Objective

The primary goal of this system is not to maximize prediction accuracy, but to **maximize business value** by answering the question:

> *Where should a company spend money to achieve the highest return from its customers?*

This project demonstrates how machine learning models can be transformed into a **real-world economic decision engine**.
