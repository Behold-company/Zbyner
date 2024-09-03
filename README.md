# Zbyner
Encrypt zipped files using binary changes method


README
English

To use the Zbyner encryption tool, follow these steps:

    Prepare Your Files: Zip the files you want to encrypt and place the ZIP file in the Data/Unlocks/ folder. This folder is located within the open-source package linked at the end of this post.

    Update Script: Open the Zbyner.py file and enter the following command:

    python

    Zbyner.Lockbyner('Name', 'New name', b'Password')

    Replace Name with the name of your ZIP file, New name with the name you want the encrypted file to have (this will be placed in the Data/Locks/ folder), and Password with your desired binary password.

    Encryption Process: This command will convert all the predefined binary characters necessary for a ZIP file into your binary password. As a result, when you attempt to open the encrypted file, you might encounter a "file damaged" error.

    Decryption: To unlock the file, use the Zbyner tool with the correct password. This will decrypt the folder, making it accessible again.

For further assistance, consult the documentation provided in the open-source package.
فارسی

برای استفاده از ابزار رمزگذاری Zbyner، مراحل زیر را دنبال کنید:

    آماده‌سازی فایل‌ها: فایل‌های مورد نظر خود را به صورت زیپ کنید و فایل زیپ شده را در فولدر Data/Unlocks/ قرار دهید. این فولدر در پکیج اوپن سورسی که در انتهای این پست لینک شده است، قرار دارد.

    به‌روزرسانی اسکریپت: فایل Zbyner.py را باز کنید و دستور زیر را وارد کنید:

    python

    Zbyner.Lockbyner('Name', 'New name', b'Password')

    جایگزین کنید Name با نام فایل زیپ شما، New name با نامی که می‌خواهید فایل رمزگذاری شده داشته باشد (این فایل در فولدر Data/Locks/ قرار خواهد گرفت)، و Password با رمز باینری مورد نظر شما.

    فرآیند رمزگذاری: این دستور تمام حروف باینری پیش‌فرض که برای یک فایل زیپ ضروری هستند را به رمز باینری شما تبدیل می‌کند. در نتیجه، وقتی که بخواهید فایل رمزگذاری شده را باز کنید، ممکن است با خطای "فایل آسیب دیده" مواجه شوید.

    رمزگشایی: برای آنلاک کردن فایل، از ابزار Zbyner با رمز درست استفاده کنید. این کار باعث رمزگشایی فولدر می‌شود و دوباره به آن دسترسی خواهید داشت.

برای کمک بیشتر، به مستندات ارائه شده در پکیج اوپن سورس مراجعه کنید.
