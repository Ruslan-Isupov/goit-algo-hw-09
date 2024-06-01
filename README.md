# Аналіз жадібного і алгоритму динамічного програмування

Час виконання алгоритмів на кожному типі даних:

| Algorithms           | Sum , n =113           | Sum, n =155            | Sum, n =540          | Sum, n =1253        |
| -------------------- | ---------------------- | ---------------------  | ---------------------| --------------------|
| Greedy_algorithm   | 0.00001 sec            | 0.00001 sec            | 0.00001 sec          |  0.00001 sec        |
| Dynamic_algorithm   | 0.00042 sec            | 0.00056 sec            | 0.00206 sec          |  0.00469 sec        |



**Жадібний алгоритм:**

Ефективність жадібного алгоритму значно перевищує ефективність алгоритму динамічного програмування. Це обумовлено часовою складністю цих алгоритмів. Головним недоліком жадібного алгоритму є те, що  він працює ефективно з невеликими сумами, але може не бути оптимальним для великих сум.

**Алгоритм динамічного програмування:**
Основним недоліком є те, що цей алгоритм вимагає більше обчислювальних ресурсів, що може призвести до збільшення часу виконання, особливо при великих сумах.

## Висновок
Результати аналізу підтверджують, що жадібний алгоритм ефективніше за часом виконання порівняно із алгоритмом динамічного програмування на обраних наборах даних. Висновки підтримують теоретичні розгляди ефективності цих алгоритмів.Вибір між цими алгоритмами залежить від конкретних вимог системи.Якщо пріоритетом є швидкість виконання і точність не є критичною, то більш оптимальним для вибору є жадібний алгоритм.Якщо ж важлива мінімальна кількість монет, оптимальним для вибору є алгоритм динамічного програмування.
