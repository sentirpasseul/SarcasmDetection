# SarcasmDetection
<div id="header">
  <p>Данный репозиторий является реформатированной версией репозитория: <a href="https://github.com/sentirpasseul/BusinessAnalist">ссылка</a>.</p>
  <p>Так как исходный код, а также структура проекта были нечитабельными и плохо оптимизированы (скорость выполнения компиляции составляла ~5 мин), было принято решение полностью переписать проект с использоваием ООП и более эффективной оптимизации.</p>
  
</div>
 


---
<div id='description-header'>
  <p>Приложение создано для определения сарказма в предложении, написанном на русском языке.</p>
</div>

---
<div id='development'>
  :desert_island: Находится в разработке
</div>

---
<div id='description'>
  <p>Целью данной работы является совершенствование методов семантического анализа естественно-языкового текста посредством разработки нейросетевой модели распознавания сарказма в тексте.
  </p>
  <br></br>
  
  <p>Признаковое пространство, используемое для определения сарказма в тексте:</p>
    <p> - Признаки, связанные с частотой. Некоторая неожиданность в тексте может указывать на наличие в тексте сарказма. Одним из индикаторов неожиданности является встречаемость в тексте одновременно как слов с высокой частотой использования, так и слов с низкой частотой;</p>
    <p> - Признаки, связанные со стилем написания. средняя частота слов, написанных в письменном стиле, средняя частота слов, написанных в устном стиле, разница первых двух признаков;</p>
    <p> - Признаки, связанные со структурой предложения. Число глаголов, существительных, прилагательных и наречий; доля глаголов, существительных, наречий и прилагательных в тексте; число всех пунктуационных символов в тексте и др;</p>
    <p> - Признаки, связанные с эмоциональной окраской предложения. Разность между максимальной положительной оценкой и средней, разность между минимальной негативной оценкой и средней;</p>
    <p> - Признаки, связанные с неоднозначностью. Одним из аспектов сарказма является неоднозначность высказывания, которое его содержит;</p>
    <p> - Признаки, связанные с интенсивностью наречий и прилагательных: суммарная интенсивность прилагательных(наречий), средняя интенсивность, максимальная интенсивность</p>
    <br></br>
    
    
  <p>Математическая модель программы:</p>
  
  <p>Алгоритм выполнения программы:</p>
  <p>1. Ввод текста</p>
  <p>2. Предобработка и анализ введенного текста</p>
  <p>3. Определение и вычисление весовых коэффициентов</p>
  <p>4. Вычисление значений по математической модели</p>
  <p>5. Сравнение результатов вычислений с датасетом </p>
</div>
