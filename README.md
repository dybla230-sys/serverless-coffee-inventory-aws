# ☕ Serverless Coffee Inventory System (AWS)

A cloud-native, serverless inventory management system built using AWS services and a React frontend.  
This project demonstrates scalable backend architecture, REST API design, and integration between serverless AWS services and a modern web application.

---

## Overview

The system allows users to view and manage coffee inventory through a REST API backed by AWS Lambda and DynamoDB.  
A React frontend consumes the API, while AWS API Gateway handles secure communication between the client and backend.

The architecture is fully serverless, meaning it scales automatically and follows a pay-as-you-go cost model.

---

## Architecture

**Flow:**

React Frontend → API Gateway → AWS Lambda → DynamoDB

**AWS Services Used:**
- AWS Lambda (serverless compute)
- Amazon DynamoDB (NoSQL database)
- Amazon API Gateway (REST API)
- AWS Amplify (frontend hosting - optional)
- AWS CloudWatch (logging and monitoring)
- AWS IAM (permissions and security)

---

## Features

- Retrieve coffee inventory items (GET)
- Add new inventory items (POST)
- Serverless backend with automatic scaling
- RESTful API design
- NoSQL data storage with DynamoDB
- React-based frontend interface
- Secure IAM role-based access

---

## Tech Stack

**Backend:**
- Python (AWS Lambda)
- DynamoDB
- API Gateway

**Frontend:**
- React.js
- Fetch API

**Cloud & DevOps:**
- AWS IAM
- CloudWatch
- GitHub

---

## Project Structure

