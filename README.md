# Presentation-happy

Учебная презентация «Концепция счастья: что делает людей счастливыми в современном мире?»
(РКСИ, группа ИС-24, Сабадаш П. А.).

Дек собран программно из SVG в нативный редактируемый PPTX с помощью пайплайна
[ppt-master](https://github.com/hugohe3/ppt-master). Все исходники (текст, заметки,
анимации, озвучка, SVG) лежат в репозитории и воспроизводимы.

## Готовые файлы (в корне репозитория)

| Файл | Что это |
| --- | --- |
| `Konceptsiya_schastya.pptx` | Основной файл: 15 слайдов, 16:9, анимации, заметки докладчика, встроенная озвучка и видео. |
| `Konceptsiya_schastya_bez_video.pptx` | Та же презентация без встроенного видео (меньше размер). |
| `Konceptsiya_schastya.pdf` | PDF-версия для печати и сдачи (15 страниц, 16:9). |

Контент целиком воспроизводится из `svg_output/` (15 страниц) + `notes/` + `audio/` +
`animations.json`. Вспомогательные и тяжёлые артефакты (фото, видео, превью, промежуточные
PPTX) в репозиторий не входят — см. `.gitignore`.

## Структура дека (15 слайдов, 16:9 1280×720)

1. `01_cover` — титульный лист (тема, автор, группа, РКСИ).
2. `01_goals` — цели и задачи работы.
3. `02_toc` — содержание (разделы).
4. `03_why` — почему тема важна.
5. `04_science` — научный подход (био-психо-социальная модель).
6. `05_physiology` — физиология счастья + видео «нейросети мозга».
7. `06_history` — история идей (6 вех: от Аристотеля до позитивной психологии).
8. `07_hedonia` — гедония и эвдемония.
9. `08_formula` — формула Селигмана (50 / 40 / 10).
10. `09_factors` — факторы, влияющие на счастье.
11. `10_easterlin` — парадокс Истерлина (плато после 75 000 $).
12. `11_education` — образование и счастье.
13. `12_digital` — цифровая среда: плюсы и минусы.
14. `13_recommendations` — практические рекомендации (6 шагов).
15. `15_sources` — выводы и источники: 5 ключевых выводов, 6 главных источников и QR-код на [полный список источников](#полный-список-источников).

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
   sustainable change // Review of General Psychology. 2005.
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

**Справочные и научно-популярные материалы (на русском)**

13. НИУ ВШЭ — публикации и исследования о субъективном благополучии.
14. УрФУ — материалы о счастье и качестве жизни.
15. Cyberleninka — научные статьи о психологии счастья.
16. Рувики, статья «Счастье».
17. Skillbox — «Что такое счастье».
18. Apteka.ru — материалы о счастье и здоровье.
19. Портал b17.ru — психология счастья.
20. РИА Новости, «Большой город», 1economic — обзорные публикации.

Изображения — Wikimedia Commons под лицензиями CC BY / CC BY-SA (авторство указано на
слайдах; исходные данные — в `images/image_sources.json`).

## Соответствие требованиям методички

* Формат 16:9, страницы не перегружены (правило «6×6»).
* Минимальный кегль текста ≥ 16.5 pt (заголовки 36 pt, тело 18 pt, подписи и сноски 16.5 pt).
* На каждом слайде — футер, номер страницы как авто-поле и корректные кредиты к фото (CC BY / CC BY-SA).
* Спикерские заметки к каждому слайду; озвучка на русском (`ru-RU-SvetlanaNeural`).
* Плавные переходы `fade` и мягкие появления блоков; титул без перехода.

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
  -f ppt169 --with-notes --narration-audio-dir audio \
  --animation-config animations.json --image-sizing display --image-quality 82 \
  -o ./Konceptsiya_schastya_bez_video.pptx
```

Встроить видео в слайд 6 и пересобрать PDF (оба скрипта в
`.agents/projects/happiness_concept_ppt169_20261007/tools/`):

```bash
python3 .../tools/embed_slide6_video.py   # берёт *_bez_video.pptx и кладёт mp4 в слайд 6
python3 .../tools/render_pdf.py           # рендерит Konceptsiya_schastya.pdf из svg_output/
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
