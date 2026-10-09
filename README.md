# Presentation-happy

Учебная презентация «Концепция счастья: что делает людей счастливыми в современном мире?»
(РКСИ, группа ИС-24, Сабадаш П. А.).

Дек собран программно из SVG в нативный редактируемый PPTX с помощью пайплайна
[ppt-master](https://github.com/hugohe3/ppt-master). Все исходники (текст, заметки,
анимации, SVG) лежат в репозитории и воспроизводимы. Озвучки в деке нет — только
редактируемые заметки докладчика.

## Готовые файлы (в корне репозитория)

| Файл | Что это |
| --- | --- |
| `Konceptsiya_schastya.pptx` | Основной файл: 15 слайдов, 16:9, анимации, Morph, заметки докладчика, анимированный GIF-постер. |
| `Konceptsiya_schastya_bez_video.pptx` | Копия основного файла без встроенного видео (в текущей версии совпадает с основным). |
| `Konceptsiya_schastya.pdf` | PDF-версия для печати и сдачи (15 страниц, 16:9). |
| `Речь_доклада.docx` | Полный текст выступления по слайдам (объём 956 слов, ~8–9 минут). |
| `Возможные_вопросы.docx` | 12 вероятных вопросов комиссии и готовые ответы. |

Контент целиком воспроизводится из `svg_output/` (15 страниц) + `notes/` +
`animations.json`. Вспомогательные и тяжёлые артефакты (фото, видео, превью,
промежуточные PPTX) в репозиторий не входят — см. `.gitignore`.

## Структура дека (15 слайдов, 16:9 1280×720)

1. `01_cover` — титульный лист (тема, автор, группа, РКСИ).
2. `01_goals` — цели и задачи работы.
3. `02_toc` — содержание (разделы).
4. `03_why` — почему тема важна.
5. `04_science` — научный подход (био-психо-социальная модель).
6. `05_physiology` — физиология счастья + анимированный GIF «нейросети мозга».
7. `06_history` — история идей (6 вех: от Аристотеля до позитивной психологии).
8. `07_hedonia` — гедония и эвдемония.
9. `08_formula` — формула Селигмана (50 / 40 / 10).
10. `09_factors` — факторы, влияющие на счастье.
11. `10_easterlin` — парадокс Истерлина (плато после 75 000 $).
12. `11_education` — образование и счастье.
13. `12_digital` — цифровая среда: плюсы и минусы.
14. `13_recommendations` — практические рекомендации (6 шагов).
15. `15_sources` — выводы: 5 ключевых выводов, краткая строка ключевых источников и QR-код на [полный список источников](#полный-список-источников).

## Полный список источников

Ниже — расширенный список литературы и материалов, на которые опирается презентация
(QR-код на слайде 15 ведёт сюда).

**Научные работы и данные**

1. Kahneman D., Deaton A. High income improves evaluation of life but not emotional
   well-being // PNAS. 2010.
2. Killingsworth M. A. Experienced well-being rises with income, even above $75,000
   per year // PNAS. 2021.
3. Kahneman D., Killingsworth M. A., et al. Income and emotional well-being: A
   conflict resolved // PNAS. 2023.
4. Seligman M. Authentic Happiness (Подлинное счастье). 2002.
5. Lyubomirsky S., Sheldon K., Schkade D. Pursuing happiness: The architecture of
   sustainable change // Review of General Psychology. 2005. — **первоисточник формулы
   50 / 40 / 10** (популяризована Селигманом).
6. Fredrickson B. L. The role of positive emotions in positive psychology: the
   broaden-and-build theory // American Psychologist. 2001.
7. Berridge K. C., Robinson T. E. Wanting, liking, and the neuroscience of
   motivation // Trends in Neurosciences. 2016.
8. Rohrer J. M., Schmukle S. C. et al. Probing the weak genetic influence on
   happiness and life satisfaction // Journal of Research in Personality. 2018.
9. Helliwell J. F. et al. World Happiness Report. Sustainable Development Solutions
   Network, ежегодно.
10. Easterlin R. A. Does economic growth improve the human lot? 1974.
11. Ehrenreich B. Bright-Sided: How Positive Thinking Is Undermining America. 2009.
12. Stevenson B., Wolfers J. Economic growth and subjective well-being // Brookings
   Papers on Economic Activity. 2008.

**Русские учёные о счастье и смысле**

13. Джидарьян И. А. Психология счастья и оптимизма. — М.: Изд-во «Институт психологии РАН», 2013.
14. Куликов Л. В. Психология настроения. — СПб.: Изд-во СПбГУ, 1997.
15. Леонтьев Д. А. Психология смысла. — М.: Смысл, 2003.
16. Рубинштейн С. Л. Бытие и сознание. — М.: Изд-во АН СССР, 1957.

**Справочные и научно-популярные материалы (на русском)**

17. НИУ ВШЭ — публикации и исследования о субъективном благополучии.
18. УрФУ — материалы о счастье и качестве жизни.
19. Cyberleninka — научные статьи о психологии счастья.
20. Рувики, статья «Счастье».
21. Skillbox — «Что такое счастье».
22. Apteka.ru — материалы о счастье и здоровье.
23. Портал b17.ru — психология счастья.
24. РИА Новости, «Большой город», 1economic — обзорные публикации.

Изображения — Wikimedia Commons под лицензиями CC BY / CC BY-SA (авторство указано на
слайдах; исходные данные — в `images/image_sources.json`).

## Соответствие требованиям методички

* Формат 16:9, страницы не перегружены (правило «6×6»).
* Минимальный кегль текста ≥ 16.5 pt (заголовки 36 pt, тело 18 pt, подписи и сноски 16.5 pt).
* На каждом слайде — футер, номер страницы как авто-поле и корректные кредиты к фото (CC BY / CC BY-SA).
* Спикерские заметки к каждому слайду; озвучки нет — текст вынесен в `Речь_доклада.docx`.
* Соотношение кеглей заголовок/текст ≤ 2 (заголовки 40 px, тело 22 px).
* Экранов «Видео» нет: на слайде 6 — анимация (GIF), подпись «Анимация: работа нейросетей мозга».
* Переходы `fade` (11 слайдов) и Morph by object (3 слайда: 08 → 10 → 12), титул без перехода.
* Объектные анимации по клику на 14 слайдах: появление, fly-in, zoom, wipe для графиков и диаграмм.
* Анимированный GIF на слайде 6; видеофайлов в пакете нет.
* В заметках слайдов 5, 6, 10, 14 добавлен русский контекст (Рубинштейн, Леонтьев, Джидарьян, Куликов, Петровский, Выготский).
* Атрибуция фото — в этом README и в `images/image_sources.json`; на слайдах — только минимальные кредиты CC BY (10 pt).

## Как пересобрать

Зависимости (опциональны для базовых инструментов, нужны для экспорта PPTX и TTS):

```bash
pip install -r .agents/skills/ppt-master/requirements.txt
```

Экспорт PPTX (переходы и анимации берутся из `animations.json`):

```bash
cd .agents/skills/ppt-master
python3 scripts/svg_to_pptx.py \
  /workspace/.../happiness_concept_ppt169_20261007 \
  -f ppt169 --with-notes \
  --animation-config animations.json --image-sizing display --image-quality 82 \
  -o ./Konceptsiya_schastya.pptx
cp ./Konceptsiya_schastya.pptx ./Konceptsiya_schastya_bez_video.pptx
```

Пересобрать PDF и превью (скрипты в
`.agents/projects/happiness_concept_ppt169_20261007/tools/`):

```bash
python3 .../tools/render_pdf.py      # рендерит Konceptsiya_schastya.pdf из svg_output/
python3 .../tools/make_poster_gif.py # собирает images/brain_neurons.gif из media/brain_neurons.mp4
python3 .../tools/make_qr_png.py     # растрирует images/qr_sources.svg -> qr_sources.png
```

Аудит готовых файлов (структура, отсутствие аудио/видео, переходы, Morph, QR):

```bash
python3 .../tools/audit_exports.py   # проверяет оба PPTX и возвращает код 1 при ошибке
```

Проверка качества SVG и готового PPTX:

```bash
python3 scripts/svg_quality_checker.py <project> --quick-generate --json
python3 scripts/pptx_delivery_check.py ./Konceptsiya_schastya.pptx
```

## Замечания по правовой части

Фотографии взяты из Wikimedia Commons под лицензиями CC BY / CC BY-SA; авторство и
лицензия указаны на слайдах с изображениями (`images/image_sources.json` — исходные данные
атрибуции). Перед публикацией вне учебного контекста проверьте условия лицензий.
