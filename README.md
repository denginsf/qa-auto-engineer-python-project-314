# QA Auto Engineer Python Project 314

[![Actions Status](https://github.com/denginsf/qa-auto-engineer-python-project-314/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/denginsf/qa-auto-engineer-python-project-314/actions) [![Coverage](https://sonarcloud.io/api/project_badges/measure?project=denginsf_qa-auto-engineer-python-project-314&metric=coverage)](https://sonarcloud.io/summary/new_code?id=denginsf_qa-auto-engineer-python-project-314)

Третий проект курса "Автоматизатор тестирования на Python" от Hexlet.

Полноценный фреймворк автоматизированного тестирования веб-приложения Task Manager (React-Admin) с применением паттерна Page Object Model, Selenium WebDriver и pytest. Проект демонстрирует навыки написания поддерживаемых и масштабируемых UI-тестов

---

## Технологии

| Инструмент | Назначение |
|-----------|------------|
| Python 3.14 | Язык программирования |
| pytest | Фреймворк для запуска тестов |
| Selenium WebDriver | Управление браузером |
| Allure | Формирование отчётов |
| Ruff | Линтер и форматтер |
| Docker + Docker Compose | для CI |

---

## Архитектура проекта

Проект построен по принципу **Page Object Model (POM)** с разделением на слои, что обеспечивает читаемость, переиспользование кода и лёгкую поддержку при изменении UI.:

- BasePage — базовый класс с общими методами (click, js_click, find_element, wait_for_backdrop и др.)
- Page классы (MainPage, TasksPage и т.д.) — методы конкретных страниц
- Actions классы — низкоуровневые действия с элементами, отделеные от Page — страница описывает *что* делать, actions — *как*
- Locators классы — локаторы полностью изолированы от логики — любое изменение UI правится в одном месте