def my_final_grade_calculation():
    final_results = {}
    
    # دریافت تعداد دانشجویان از کاربر
    num_students = int(input("تعداد دانشجویان را وارد کنید: "))
    
    # دریافت اطلاعات هر دانشجو
    for _ in range(num_students):
        # دریافت نام دانشجو و تبدیل آن به حروف کوچک
        name = input("نام دانشجو را وارد کنید: ").lower()

        # دریافت نمرات آزمون‌های کوچک (q1 تا q6)
        quizzes = []
        for i in range(1, 7):
            quiz = int(input(f"نمره آزمون {i} (q{i}) را وارد کنید: "))
            quizzes.append(quiz)
        
        # دریافت نمرات تکالیف (a1 تا a4)
        assignments = []
        for i in range(1, 5):
            assignment = int(input(f"نمره تکلیف {i} (a{i}) را وارد کنید: "))
            assignments.append(assignment)
        
        # دریافت نمره میان ترم
        midterm = int(input("نمره میان ترم را وارد کنید: "))
        
        # دریافت نمره امتحان نهایی
        final_exam = int(input("نمره امتحان نهایی را وارد کنید: "))
        
        # محاسبه میانگین نمرات
        quiz_average = sum(quizzes) / len(quizzes)  # میانگین آزمون‌ها
        assignment_average = sum(assignments) / len(assignments)  # میانگین تکالیف
        
        # محاسبه نمره نهایی با توجه به وزن‌دهی‌ها
        final_grade = (quiz_average * 0.3) + (assignment_average * 0.2) + (midterm * 0.2) + (final_exam * 0.3)
        
        # تعیین وضعیت قبولی یا مردودی
        if final_grade >= 60:
            final_results[name] = "PASS"
        else:
            final_results[name] = "Fail"
    
    return final_results

# فراخوانی تابع
results = my_final_grade_calculation()
print(results)
