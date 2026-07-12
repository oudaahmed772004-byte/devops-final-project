# دليل التنفيذ والتسليم — خطوة بخطوة

هذا الملف **ليس جزءًا من التسليم النهائي** — احذفه من المستودع قبل الرفع
النهائي (أو اتركه، لن يضرّك، لكن الأفضل حذفه). الهدف منه إرشادك بالضبط
شو تعمل بالطرفية عشان تولّد نتائج حقيقية ولقطات شاشة من عندك.

> ملاحظة عامة: كل أمر تشوفه بالأسفل شغّله بنفسك في طرفية (Terminal) حقيقية
> على جهازك (Linux أو WSL على ويندوز أو macOS)، وخذ لقطة شاشة (Screenshot)
> بعد كل نتيجة مطلوبة.

---

## 0) التحضير

1. فك ضغط الملف المرفق في مكان يسهل الوصول له، مثلًا:
   ```bash
   cd ~/Desktop
   unzip devops-final-project.zip
   cd devops-final-project
   ```
2. تأكد إن عندك Git و Docker مثبتين:
   ```bash
   git --version
   docker --version
   ```

---

## Module 1 — Linux Basics

```bash
cd ~/Desktop/devops-final-project
ls -R          # 📸 لقطة شاشة 1: هيكل المجلدات
```

```bash
cd scripts
chmod +x info.sh
./info.sh      # 📸 لقطة شاشة 2: ناتج info.sh
cd ..
```

```bash
cd scripts
chmod +x backup.sh
./backup.sh    # 📸 لقطة شاشة 3: "Backup complete. 3 file(s) copied."
ls ../backup   # تحقق من وجود الملفات المنسوخة
cd ..
```

```bash
mkdir -p logs
ping -c 4 google.com > logs/network.log
echo "----- curl output -----" >> logs/network.log
curl -sI https://example.com >> logs/network.log
cat logs/network.log   # 📸 لقطة شاشة 4: محتوى network.log
```

---

## Module 2 — Git Version Control

```bash
git init
git config user.name "اسمك الكامل"
git config user.email "بريدك@example.com"
```

عدّل `README.md` وحط اسمك ورقمك الجامعي مكان `[ضع اسمك...]`، ثم:

```bash
git add README.md
git commit -m "Initial commit: project structure created"
git log        # 📸 لقطة شاشة 5
```

```bash
git add app/notes1.txt
git commit -m "Add project idea notes file"

git add app/notes2.txt
git commit -m "Add meeting notes file"

git add app/notes3.txt
git commit -m "Add submission reminder notes file"

git log --oneline   # 📸 لقطة شاشة 6
```

```bash
git checkout -b feature/add-script
git add scripts/hello.sh
git commit -m "Add hello.sh greeting script"

git checkout main       # أو master حسب اسم فرعك الرئيسي
git merge feature/add-script
git log --oneline --graph   # 📸 لقطة شاشة 7
```

```bash
# تعديل ملف موجود لإظهار Undo & Inspect
echo "# extra line for demo" >> README.md
git add README.md
git restore --staged README.md
git diff        # 📸 لقطة شاشة 8: يظهر التغيير غير المرحّل (unstaged)
```

> ملاحظة: لو ما صار Merge Conflict، هذا طبيعي تمامًا (لأن hello.sh ملف
> جديد بالكامل) — لا تحتاج تفتعل تعارضًا، فقط وثّق أن الدمج تم بنجاح.

---

## Module 3 — GitHub — Remote Work

1. روح لـ https://github.com وسوّي مستودع جديد (New repository):
   - الاسم: `devops-final-project`
   - Public
   - **لا** تضيف README أو .gitignore من واجهة GitHub (عندك أصلًا).

2. اربط المستودع المحلي بالبعيد وارفع:
   ```bash
   git remote add origin https://github.com/USERNAME/devops-final-project.git
   git branch -M main
   git push -u origin main
   ```
   📸 لقطة شاشة 9: صفحة المستودع على GitHub بعد الرفع.

3. فرع جديد للملاحظات:
   ```bash
   git checkout -b feature/github-setup
   ```
   أنشئ ملف `GITHUB_NOTES.md` بالمحتوى التالي (أو بأسلوبك):
   ```markdown
   # GitHub Notes

   GitHub is a cloud-based platform for hosting Git repositories. It allows
   developers to collaborate, track changes, review code through Pull
   Requests, and automate workflows using GitHub Actions. In this project,
   it was used to host the remote repository, manage branches, and run CI.
   ```
   ```bash
   git add GITHUB_NOTES.md
   git commit -m "Add GitHub notes explaining its purpose"
   git push origin feature/github-setup
   ```
   📸 لقطة شاشة 10: الفرع ظاهر تحت تبويب Branches على GitHub.

4. افتح Pull Request من `feature/github-setup` إلى `main` من واجهة GitHub،
   اكتب عنوان ووصف واضح، ثم اضغط **Merge pull request**.
   📸 لقطة شاشة 11: صفحة تأكيد الدمج.

5. تحقق من الاستنساخ (Clone) في مكان آخر:
   ```bash
   cd ~/Desktop
   git clone https://github.com/USERNAME/devops-final-project.git devops-final-clone
   cd devops-final-clone
   git log --oneline   # 📸 لقطة شاشة 12
   ls -R
   ```

6. بعدها ارجع لمجلدك الأصلي وحدّث فرع main محليًا:
   ```bash
   cd ~/Desktop/devops-final-project
   git checkout main
   git pull origin main
   ```

---

## Module 4 — Docker

```bash
cd ~/Desktop/devops-final-project
docker build -f docker/Dockerfile -t USERNAME/notes-info-server:v1.0 .
```
📸 لقطة شاشة 13: نجاح عملية البناء (Build).

```bash
docker images   # 📸 لقطة شاشة 14: الصورة موجودة بالاسم والتاغ الصحيح
```

```bash
docker run -d -p 5000:5000 \
  -e APP_MESSAGE="Hello from my DevOps project!" \
  --name notes-info-server \
  USERNAME/notes-info-server:v1.0

curl http://localhost:5000/
curl http://localhost:5000/health
```
📸 لقطة شاشة 15: ناتج curl يوضح إن التطبيق شغال.

```bash
docker ps   # تحقق إن الحاوية Healthy بعد ٣٠ ثانية تقريبًا
```

عدّل قسم "Docker" بملف `README.md` (موجود جاهز) وبدّل `yourname` باسمك،
وأضف لقطات الشاشة (13، 14، 15) تحت هذا القسم.

---

## Module 5 — GitHub Actions (CI/CD)

الملف `.github/workflows/ci.yml` جاهز ومضاف مسبقًا. فقط ارفعه:

```bash
git add .
git commit -m "Add GitHub Actions CI workflow"
git push origin main
```

1. روح لتبويب **Actions** بمستودعك على GitHub.
2. تأكد إن الـ Workflow اشتغل وظهرت علامة ✅ خضراء.
3. 📸 لقطة شاشة 16: صفحة الـ run الناجح.
4. أضف اللقطة تحت قسم "GitHub Actions" بملف README.md مع جملة توضّح إيش
   يعمل الـ Workflow (موجودة جاهزة بالقالب).

---

## الخطوات الأخيرة قبل التسليم

1. احذف ملف `SUBMISSION_GUIDE.md` هذا من المستودع (اختياري لكن يفضّل):
   ```bash
   git rm SUBMISSION_GUIDE.md
   git commit -m "Remove internal submission guide"
   git push origin main
   ```
2. تأكد إن كل الأقسام بـ README.md معبّاة (اسمك، رقمك، الوصف، اللقطات).
3. تأكد إن المستودع **Public** فعلاً (Settings → General → Danger Zone).
4. حضّر التقرير النهائي (Word أو PDF) يحتوي:
   - كل لقطات الشاشة (16 لقطة تقريبًا حسب القائمة أعلاه) مرتبة حسب الموديول.
   - شرح مختصر لكل خطوة (يقدر يكون نفس نص README مع لقطات إضافية).
5. سلّم على Moodle:
   - رابط مستودع GitHub العام.
   - ملف التقرير (Word/PDF).

بالتوفيق! 🚀
