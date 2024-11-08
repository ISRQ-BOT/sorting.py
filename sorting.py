import random
import time

# خوارزمية فرز التحديد
def selection_sort(arr):
    comparisons = 0
    movements = 0
    start_time = time.time()
    
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):      
            comparisons += 1
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        movements += 1
    
    end_time = time.time()
    execution_time = end_time - start_time
    return comparisons, movements, execution_time

# خوارزمية فرز الفقاعة
def bubble_sort(arr):
    comparisons = 0
    movements = 0
    start_time = time.time()
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                movements += 1
                swapped = True
        if not swapped:
            break
    
    end_time = time.time()
    execution_time = end_time - start_time
    return comparisons, movements, execution_time

# خوارزمية فرز الإدراج
def insertion_sort(arr):
    comparisons = 0
    movements = 0
    start_time = time.time()
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            comparisons += 1
            arr[j + 1] = arr[j]
            movements += 1
            j -= 1
        arr[j + 1] = key
        movements += 1
        if j >= 0:
            comparisons += 1  # للمقارنة الأخيرة التي تخرج من الحلقة
    
    end_time = time.time()
    execution_time = end_time - start_time
    return comparisons, movements, execution_time

# دالة لإنشاء مصفوفات بترتيبات مختلفة
def generate_arrays(size):
    random_array = [random.randint(1, 100) for _ in range(size)]
    ascending_array = sorted(random_array)
    descending_array = sorted(random_array, reverse=True)
    return random_array, ascending_array, descending_array

# دالة لتشغيل الاختبارات وجمع المتوسطات
def run_algorithm_tests(algorithm, arr, num_tests=30):
    total_comparisons = 0
    total_movements = 0
    total_time = 0
    
    for _ in range(num_tests):
        arr_copy = arr[:]
        comparisons, movements, execution_time = algorithm(arr_copy)
        
        total_comparisons += comparisons
        total_movements += movements
        total_time += execution_time
    
    avg_comparisons = total_comparisons / num_tests
    avg_movements = total_movements / num_tests
    avg_time = total_time / num_tests
    
    return avg_comparisons, avg_movements, avg_time

# دالة لتنظيم الاختبارات على الأحجام المختلفة وأنواع المصفوفات
def compare_algorithms(sizes, num_tests=30):
    algorithms = {
        "Selection Sort": selection_sort,
        "Bubble Sort": bubble_sort,
        "Insertion Sort": insertion_sort
    }
    
    results = {alg: {"Random": {}, "Ascending": {}, "Descending": {}} for alg in algorithms.keys()}
    
    for size in sizes:
        print(f"\n=== Array Size: {size} ===")
        
        # إنشاء مصفوفات عشوائية، تصاعدية وتنازلية لكل حجم
        random_array, ascending_array, descending_array = generate_arrays(size)
        
        for name, algorithm in algorithms.items():
            print(f"\n{name} started")  # رسالة البداية
            
            for arr, order in zip([random_array, ascending_array, descending_array], ["Random", "Ascending", "Descending"]):
                avg_comparisons, avg_movements, avg_time = run_algorithm_tests(algorithm, arr, num_tests)
                
                # حفظ النتائج في القاموس
                results[name][order][size] = {
                    "Avg Comparisons": avg_comparisons,
                    "Avg Movements": avg_movements,
                    "Avg Time (s)": avg_time
                }
                
                # عرض النتائج في الجدول
                print(f"Order: {order}, Size: {size}, Avg Comparisons: {avg_comparisons:.2f}, Avg Movements: {avg_movements:.2f}, Avg Time: {avg_time:.5f} seconds")
    
    return results

# تنفيذ التجارب على أحجام المصفوفات المختلفة
sizes = [1000, 5000, 10000]
print("=== Starting Sorting Tests ===")  # رسالة بداية
results = compare_algorithms(sizes, num_tests=30)
print("=== Sorting Tests Completed ===")  # رسالة نهاية
