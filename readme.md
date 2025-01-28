# Порівняльний аналіз алгоритмів сортування

## приклад виконання

### Size: 1000, Type: random
### Insertion Sort: 0.020021s
### Merge Sort: 0.001730s
### Timsort: 0.000096s

### Size: 1000, Type: sorted
### Insertion Sort: 0.000104s
### Merge Sort: 0.001371s
### Timsort: 0.000009s

### Size: 1000, Type: reversed
### Insertion Sort: 0.039059s
### Merge Sort: 0.001332s
### Timsort: 0.000010s

### Size: 5000, Type: random
### Insertion Sort: 0.529882s
### Merge Sort: 0.009921s
### Timsort: 0.000515s

### Size: 5000, Type: sorted
### Insertion Sort: 0.000535s
### Merge Sort: 0.008166s
### Timsort: 0.000039s

### Size: 5000, Type: reversed
### Insertion Sort: 1.029095s
### Merge Sort: 0.007792s
### Timsort: 0.000042s

### Size: 10000, Type: random
### Insertion Sort: 2.170616s
### Merge Sort: 0.022390s
### Timsort: 0.001183s

### Size: 10000, Type: sorted
### Insertion Sort: 0.001080s
### Merge Sort: 0.017315s
### Timsort: 0.000126s

### Size: 10000, Type: reversed
### Insertion Sort: 4.387064s
### Merge Sort: 0.016941s
### Timsort: 0.000117s

### Size: 20000, Type: random
### Insertion Sort: 8.918642s
### Merge Sort: 0.045077s
### Timsort: 0.002474s

### Size: 20000, Type: sorted
### Insertion Sort: 0.002038s
### Merge Sort: 0.036169s
### Timsort: 0.000242s

### Size: 20000, Type: reversed
### Insertion Sort: 17.136409s
### Merge Sort: 0.038346s
### Timsort: 0.000320s

#### Сортування вставками:
Показало найгірші результати на великих масивах, особливо для зворотно відсортованих даних.
 Працює швидко лише на малих або вже відсортованих масивах.

#### Сортування злиттям:
 Значно швидше за сортування вставками, особливо на великих масивах, завдяки складності O(n log n).
Добре працює для всіх типів даних (випадкових, відсортованих і зворотних), але потребує додаткової пам’яті для злиття частин масиву.

#### Timsort (вбудована функція sorted):
Найефективніший алгоритм серед трьох.
Показав найкращі результати на всіх типах даних і розмірах масивів.
Час виконання значно менший завдяки оптимізації для частково відсортованих масивів та комбінуванню сортування злиттям і вставками.