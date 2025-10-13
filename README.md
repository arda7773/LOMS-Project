# LOMS Monorepo Scaffold

Bu proje, arkadaşının tarif ettiği yapıya göre oluşturulmuş **monorepo** örneğidir:

```
loms-project/
├─ .gitignore
├─ README.md
├─ settings.gradle
├─ build.gradle             (root: ortak ayarlar)
├─ core/                    (temel özellikler & paylaşılan kod)
│  ├─ build.gradle
│  └─ src/main/java/com/example/core/
│     └─ Greeter.java
├─ loms/                    (ana sistem / ilk uygulama)
│  ├─ build.gradle
│  └─ src/main/java/com/example/loms/
│     └─ Main.java
└─ apps/                    (ileride yeni uygulamalar eklemek için boş klasör)
```

## Hızlı Başlangıç
```bash
# 1) Gradle wrapper ekleme (lokalinizde çalıştırın)
gradle wrapper

# 2) Derleme
./gradlew build

# 3) Çalıştırma
./gradlew :loms:run
```

## Mantık
- `core`: Ortak modeller, yardımcılar ve domain mantığı.
- `loms`: `core`a bağımlı çalışan ilk app.
- `apps/`: Sonradan eklemek istediğiniz diğer app'ler için yer.
- `.gitignore`: Reponuza gereksiz build çıktıları ve IDE dosyaları gitmesin diye.

## Yeni bir app eklemek
1. `apps/my-new-app` klasörü açın (Gradle module).
2. `settings.gradle` içine `include("apps:my-new-app")` ekleyin.
3. `apps/my-new-app/build.gradle` içinde `implementation(project(":core"))` ile `core`a bağımlı yapın.