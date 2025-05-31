# تثبيت ونشر ZeroHunter على GitHub

هذا الدليل يشرح كيفية تثبيت ونشر مشروع ZeroHunter على GitHub.

## المتطلبات الأساسية

قبل البدء، تأكد من توفر المتطلبات التالية:

1. حساب على GitHub
2. Git مثبت على جهازك
3. Python 3.8 أو أحدث
4. pip (مدير حزم Python)

## خطوات نشر المشروع على GitHub

### 1. إنشاء مستودع جديد على GitHub

1. قم بتسجيل الدخول إلى حسابك على GitHub
2. انقر على زر "+" في الزاوية العلوية اليمنى واختر "New repository"
3. أدخل اسم المستودع: `zerohunter`
4. أضف وصفًا للمشروع: `ZeroHunter - أداة لينكس متقدمة للكشف عن هجمات Zero-Day`
5. اختر ما إذا كنت تريد أن يكون المستودع عامًا أو خاصًا
6. اختر "Initialize this repository with a README" إذا كنت تريد إنشاء ملف README تلقائيًا
7. اختر ترخيص GPL-3.0
8. انقر على "Create repository"

### 2. تهيئة المستودع المحلي

1. قم بفك ضغط ملف `zerohunter.zip` في مجلد على جهازك
2. افتح نافذة الطرفية (Terminal) وانتقل إلى المجلد الذي فككت فيه الملفات:

```bash
cd /path/to/zerohunter
```

3. قم بتهيئة مستودع Git محلي:

```bash
git init
```

4. أضف جميع الملفات إلى منطقة التحضير:

```bash
git add .
```

5. قم بعمل commit للتغييرات:

```bash
git commit -m "النسخة الأولية من ZeroHunter"
```

### 3. ربط المستودع المحلي بمستودع GitHub

1. قم بربط المستودع المحلي بمستودع GitHub الذي أنشأته:

```bash
git remote add origin https://github.com/YOUR_USERNAME/zerohunter.git
```

استبدل `YOUR_USERNAME` باسم المستخدم الخاص بك على GitHub.

2. قم بدفع التغييرات إلى GitHub:

```bash
git push -u origin main
```

أو إذا كان الفرع الرئيسي هو "master":

```bash
git push -u origin master
```

### 4. التحقق من المستودع على GitHub

1. انتقل إلى صفحة المستودع على GitHub للتأكد من أن جميع الملفات قد تم رفعها بنجاح

## تثبيت ZeroHunter

### التثبيت باستخدام pip

الطريقة الأسهل لتثبيت ZeroHunter هي استخدام pip:

```bash
# تثبيت من PyPI (عندما يتم نشر الحزمة)
pip install zerohunter

# أو التثبيت مباشرة من GitHub
pip install git+https://github.com/YOUR_USERNAME/zerohunter.git
```

استبدل `YOUR_USERNAME` باسم المستخدم الخاص بك على GitHub.

### التثبيت من المصدر

يمكنك أيضًا تثبيت ZeroHunter من المصدر:

1. قم بتنزيل أو استنساخ المستودع:

```bash
git clone https://github.com/YOUR_USERNAME/zerohunter.git
cd zerohunter
```

2. قم بتثبيت الحزمة في وضع التطوير:

```bash
pip install -e .
```

### التثبيت باستخدام حزمة .deb (لأنظمة Ubuntu/Debian)

لإنشاء حزمة .deb وتثبيتها:

1. قم بتثبيت الأدوات اللازمة:

```bash
sudo apt-get install python3-stdeb dh-python
```

2. قم بإنشاء حزمة .deb:

```bash
python3 setup.py --command-packages=stdeb.command bdist_deb
```

3. قم بتثبيت الحزمة:

```bash
sudo dpkg -i deb_dist/python3-zerohunter_0.1.0-1_all.deb
sudo apt-get install -f  # لتثبيت التبعيات المفقودة
```

## استخدام ZeroHunter

بعد التثبيت، يمكنك تشغيل ZeroHunter بالطرق التالية:

### وضع الواجهة الرسومية

```bash
zerohunter
```

### وضع سطر الأوامر

```bash
zerohunter --cli
```

### أمثلة على الاستخدام

```bash
# فحص النظام
zerohunter --scan --system

# فحص الشبكة
zerohunter --scan --network

# فحص ملف
zerohunter --scan --file /path/to/file

# فحص مجلد
zerohunter --scan --directory /path/to/directory

# فحص عملية
zerohunter --scan --process 1234

# فحص الذاكرة
zerohunter --scan --memory

# إنشاء تقرير
zerohunter --report --format pdf --output /path/to/report.pdf
```

## تطوير ZeroHunter

إذا كنت ترغب في المساهمة في تطوير ZeroHunter، اتبع الخطوات التالية:

1. قم بإنشاء بيئة Python افتراضية:

```bash
python3 -m venv venv
source venv/bin/activate  # على Linux/macOS
# أو
venv\Scripts\activate  # على Windows
```

2. قم بتثبيت متطلبات التطوير:

```bash
pip install -r requirements.txt
pip install -e .
```

3. قم بإجراء التغييرات وإضافة الاختبارات إذا لزم الأمر

4. قم بالتأكد من أن جميع الاختبارات تمر:

```bash
pytest
```

5. قم بإرسال طلب سحب (Pull Request) مع تغييراتك

## الترخيص

هذا المشروع متاح تحت ترخيص GPL-3.0.

---

# Installing and Publishing ZeroHunter on GitHub

This guide explains how to install and publish the ZeroHunter project on GitHub.

## Prerequisites

Before starting, make sure you have the following:

1. A GitHub account
2. Git installed on your machine
3. Python 3.8 or newer
4. pip (Python package manager)

## Steps to Publish the Project on GitHub

### 1. Create a New Repository on GitHub

1. Log in to your GitHub account
2. Click the "+" button in the top-right corner and select "New repository"
3. Enter the repository name: `zerohunter`
4. Add a description: `ZeroHunter - Advanced Linux Tool for Zero-Day Attack Detection`
5. Choose whether you want the repository to be public or private
6. Select "Initialize this repository with a README" if you want to create a README file automatically
7. Choose the GPL-3.0 license
8. Click "Create repository"

### 2. Initialize the Local Repository

1. Extract the `zerohunter.zip` file to a folder on your machine
2. Open a terminal window and navigate to the folder where you extracted the files:

```bash
cd /path/to/zerohunter
```

3. Initialize a local Git repository:

```bash
git init
```

4. Add all files to the staging area:

```bash
git add .
```

5. Commit the changes:

```bash
git commit -m "Initial version of ZeroHunter"
```

### 3. Link the Local Repository to the GitHub Repository

1. Link the local repository to the GitHub repository you created:

```bash
git remote add origin https://github.com/YOUR_USERNAME/zerohunter.git
```

Replace `YOUR_USERNAME` with your GitHub username.

2. Push the changes to GitHub:

```bash
git push -u origin main
```

Or if the main branch is "master":

```bash
git push -u origin master
```

### 4. Verify the Repository on GitHub

1. Go to the repository page on GitHub to ensure that all files have been uploaded successfully

## Installing ZeroHunter

### Installation using pip

The easiest way to install ZeroHunter is using pip:

```bash
# Install from PyPI (when the package is published)
pip install zerohunter

# Or install directly from GitHub
pip install git+https://github.com/YOUR_USERNAME/zerohunter.git
```

Replace `YOUR_USERNAME` with your GitHub username.

### Installation from source

You can also install ZeroHunter from source:

1. Download or clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/zerohunter.git
cd zerohunter
```

2. Install the package in development mode:

```bash
pip install -e .
```

### Installation using .deb package (for Ubuntu/Debian systems)

To create and install a .deb package:

1. Install the necessary tools:

```bash
sudo apt-get install python3-stdeb dh-python
```

2. Create a .deb package:

```bash
python3 setup.py --command-packages=stdeb.command bdist_deb
```

3. Install the package:

```bash
sudo dpkg -i deb_dist/python3-zerohunter_0.1.0-1_all.deb
sudo apt-get install -f  # to install missing dependencies
```

## Using ZeroHunter

After installation, you can run ZeroHunter in the following ways:

### GUI Mode

```bash
zerohunter
```

### CLI Mode

```bash
zerohunter --cli
```

### Usage Examples

```bash
# Scan system
zerohunter --scan --system

# Scan network
zerohunter --scan --network

# Scan file
zerohunter --scan --file /path/to/file

# Scan directory
zerohunter --scan --directory /path/to/directory

# Scan process
zerohunter --scan --process 1234

# Scan memory
zerohunter --scan --memory

# Generate report
zerohunter --report --format pdf --output /path/to/report.pdf
```

## Developing ZeroHunter

If you want to contribute to ZeroHunter development, follow these steps:

1. Create a Python virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # on Linux/macOS
# or
venv\Scripts\activate  # on Windows
```

2. Install development requirements:

```bash
pip install -r requirements.txt
pip install -e .
```

3. Make your changes and add tests if necessary

4. Ensure all tests pass:

```bash
pytest
```

5. Submit a Pull Request with your changes

## License

This project is available under the GPL-3.0 license.
