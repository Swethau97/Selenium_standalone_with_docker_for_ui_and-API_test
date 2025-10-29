---

# 🧪 Dockerized Selenium & Pytest Framework for UI + API Testing

This project demonstrates how to **containerize Selenium-based UI tests and API tests** using **Docker** and **Pytest**.
It eliminates local setup dependencies, provides a clean and reproducible test environment, and can be easily integrated into **CI/CD pipelines** (like GitHub Actions or Jenkins).

---

## 🧭 Overview

Normally, running Selenium tests locally requires:

* Installing Chrome/Firefox browsers
* Managing WebDriver versions
* Dealing with environment conflicts

By using **Docker containers**, this framework:

* Spins up a **Selenium Standalone Chrome** container (which already has Chrome + ChromeDriver configured).
* Runs all tests from a **Pytest container** that communicates with the Selenium container remotely through the **WebDriver endpoint** (`http://selenium:4444/wd/hub`).
* Supports **headless testing**, making it perfect for automation pipelines.

This setup ensures **consistent, isolated, and repeatable** test executions across all environments.

---

## 🧩 How It Works

### ⚙️ Components

| Component                             | Purpose                                                                                                  |
| ------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| **Dockerfile**                        | Builds a Python-based image for running Pytest.                                                          |
| **docker-compose.yml**                | Orchestrates Selenium and Pytest containers to work together.                                            |
| **conftest.py**                       | Creates a Singleton WebDriver instance that automatically detects whether tests run locally or remotely. |
| **test files (e.g., test_create.py)** | Contain the actual API/UI test logic using the `driver` fixture.                                         |

---

## 🔍 Execution Flow

### Local vs Docker Execution

1. **Local Run**

   * The framework detects that there is **no `SELENIUM_URL`** environment variable.
   * It launches a **local Chrome browser** using ChromeDriver.
   * Used mainly for quick debugging or single test runs on a developer’s machine.

2. **Docker Run**

   * Docker Compose sets the environment variable `SELENIUM_URL=http://selenium:4444/wd/hub`.
   * The test container connects to the **Selenium Standalone Chrome** container using this URL.
   * All browser operations happen **inside the Selenium container**, not on your host system.

---

## 🧠 High-Level Architecture

```
                   ┌────────────────────────┐
                   │       Developer        │
                   │ (Push code to GitHub)  │
                   └────────────┬───────────┘
                                │
                                ▼
          ┌──────────────────────────────────────────┐
          │             Docker Compose               │
          │------------------------------------------│
          │   1️⃣ selenium/standalone-chrome          │
          │      • Runs headless Chrome browser      │
          │      • Exposes port 4444 for WebDriver   │
          │                                          │
          │   2️⃣ pytest_app (your tests)             │
          │      • Runs Pytest inside container      │
          │      • Connects to Selenium container    │
          │------------------------------------------│
          │   Shared Network: test <-> selenium      │
          └──────────────────────────────────────────┘
                                │
                                ▼
                 ✅ Results logged and reported
```

---

## 📜 How the `conftest.py` Works

* It follows the **Singleton Design Pattern** — ensures only one WebDriver instance is created throughout a test session.
* Checks for an environment variable `SELENIUM_URL`.
* If it exists → connects remotely to Selenium inside Docker.
* If not → runs Chrome locally.
* Handles setup and teardown automatically via Pytest fixtures.

This makes your test scripts extremely **clean**, since you can directly use the `driver` fixture without worrying about setup code.

---

## 🧰 Technologies Used

| Technology             | Purpose                                                |
| ---------------------- | ------------------------------------------------------ |
| **Python 3.11**        | Base language for automation and testing               |
| **Pytest**             | Testing framework for execution and reporting          |
| **Selenium WebDriver** | Browser automation library                             |
| **Docker**             | Containerization tool for isolated environments        |
| **Docker Compose**     | Tool to manage multiple containers (Selenium + Pytest) |

---

## 🚀 How to Run the Tests

### 🐳 Step 1: Build and Start Containers

```bash
docker compose up --build
```

👉 This will:

* Pull the **selenium/standalone-chrome** image.
* Build your test container from the **Dockerfile**.
* Run Pytest automatically once Selenium is up and healthy.

---

### 🧹 Step 2: Stop Containers After Execution

```bash
docker compose down
```

---

### 🧪 Step 3: Run Specific Tests (Optional)

If you want to run specific test files, modify the command in `docker-compose.yml` or override it like this:

```bash
docker compose run pytest_app pytest tests/test_create.py -v
```

---

## 🪄 Advantages of This Setup

### 🐳 **Docker Advantages**

1. **Environment Consistency:** Same setup on every machine or CI server.
2. **No Local Dependencies:** No need to install browsers or drivers manually.
3. **Reproducibility:** One command (`docker compose up`) spins up the entire test environment.
4. **Scalable:** Can easily extend to Selenium Grid for parallel tests.
5. **CI/CD Friendly:** Integrates seamlessly with GitHub Actions, Jenkins, GitLab CI, etc.

---

### 🌐 **Selenium Standalone Chrome Advantages**

1. Comes with Chrome + ChromeDriver pre-installed.
2. Runs tests in **headless mode** — faster and ideal for CI servers.
3. Supports multiple containers or a full Selenium Grid setup.
4. Simplifies test setup — no OS/browser compatibility issues.

---

### ⚡ **Pytest Advantages**

1. Clean and readable test syntax.
2. Built-in fixture system (e.g., `driver` fixture).
3. Easy integration with HTML or JUnit reports.
4. Supports parameterization and modular test design.

---

## 🔄 CI/CD Integration Concept

Here’s how your setup fits into a continuous integration pipeline:

```
 Developer Commits Code
          │
          ▼
   GitHub Actions / Jenkins Trigger
          │
          ▼
  Build Docker Image (pytest_app)
          │
          ▼
  Start Selenium + Pytest Containers
          │
          ▼
  Run Tests → Collect Reports → Notify
```

This pipeline ensures that every new change is tested automatically in an isolated, predictable environment.

---


