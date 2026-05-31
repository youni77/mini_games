# Timed Multiplication Quiz

This project is a simple multiplication quiz game written in Python. The player must answer randomly generated multiplication questions within 10 seconds.

The repository contains two different implementations:

### 1. Threading Version

The first version uses Python's built-in `threading` module to simulate a time limit. This implementation was created as an experiment to explore multithreading and understand how user input behaves when handled in a separate thread.

However, Python's standard `input()` function cannot be forcibly stopped by a thread. As a result, although the program can detect that the time limit has expired, the input thread may still remain active in the background.

### 2. Input Timeout Version

The second version uses the `inputimeout` library, which provides a cleaner and more reliable way to enforce a time limit on user input.

I included this version to demonstrate a practical solution to the limitations of the threading approach. By comparing both implementations, it becomes easier to understand the challenges of handling timed input in Python and the advantages of using specialized libraries when appropriate.

## Learning Goals

* Working with random number generation
* Using loops and conditionals
* Exploring multithreading with `threading`
* Understanding the limitations of `input()`
* Handling exceptions
* Comparing custom solutions with third-party libraries
* Building simple terminal-based games



# بازی آزمون ضرب با محدودیت زمانی

این پروژه یک بازی سادهٔ ضرب در پایتون است که در آن بازیکن باید به سوالات ضربی که به صورت تصادفی تولید می‌شوند، در مدت ۱۰ ثانیه پاسخ دهد.

در این پوشه دو پیاده‌سازی متفاوت از بازی قرار داده شده است:

### نسخهٔ اول: استفاده از Threading

در این نسخه از ماژول داخلی `threading` پایتون استفاده شده است تا محدودیت زمانی برای پاسخ دادن شبیه‌سازی شود.

هدف از پیاده‌سازی این نسخه، آشنایی با مفهوم چندنخی (Multithreading) و بررسی نحوهٔ کار تابع `input()` در کنار رشته‌های مختلف بود.

در طول توسعهٔ پروژه متوجه شدم که تابع `input()` را نمی‌توان به سادگی متوقف کرد. به همین دلیل، با وجود اینکه برنامه می‌تواند پایان زمان را تشخیص دهد، رشته‌ای که منتظر دریافت ورودی است همچنان فعال باقی می‌ماند.

### نسخهٔ دوم: استفاده از کتابخانهٔ inputimeout

در نسخهٔ دوم از کتابخانهٔ `inputimeout` استفاده شده است. این کتابخانه امکان تعیین محدودیت زمانی واقعی برای دریافت ورودی را فراهم می‌کند.

دلیل استفاده از این کتابخانه، رفع محدودیت‌های روش مبتنی بر `threading` و ارائهٔ یک راه‌حل مطمئن‌تر برای مدیریت زمان پاسخ‌گویی کاربر بود.


