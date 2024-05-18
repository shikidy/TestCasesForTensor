# Тесты для тзшки

### В проекте использовалась библиотека Allure для создания отчетов о результатах тестирования.
### Все зависимости указаны в файле requirements.txt 

## Запуск
### Без allure
```bash
pytest
```
### С allure
```bash
pytest --alluredir=./allure_results
allure serve .\allure_results\     
```
