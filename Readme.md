# Prompt Guard

Этот проект представляет собой реализацию системы защиты от инъекций в текстовые запросы, использующую модель DeBERTa для классификации.

## Описание

Код в этом репозитории был заимствован из [Melodiz/prompt-guard](https://github.com/Melodiz/prompt-guard). Проект использует библиотеку FastAPI для создания API, а также библиотеку Transformers от Hugging Face для работы с предобученной моделью.

## Запуск

Для запуска проекта необходимо склонировать его и запустить через докер

```
git clone https://github.com/RostOs4/test_promt_guard.git
cd test_promt_guard
docker-compose up --build
```