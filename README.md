# SarcasmDetection
<div id="header">
  <div><p><h2>:warning: Данный репозиторий является реформатированной версией репозитория: <a href="https://github.com/sentirpasseul/BusinessAnalist">ссылка</a>.</h2></p></div>
  <p><h4>Так как исходный код, а также структура проекта были нечитабельными и плохо оптимизированы (скорость выполнения компиляции составляла ~5 мин), было принято решение полностью переписать проект с использоваием ООП и более эффективной оптимизации.</h4></p>
  <br></br>
  
  <h4>:desert_island: Находится в разработке</h4>
  
</div>

---
<div id='development'>
  
  
  <p><h3>Следующие goals:</h3></p>
  <p><h4>:triangular_flag_on_post: Переписать полностью программу под новый стиль с pep8</h4></p>
  <p><h4>:triangular_flag_on_post: Подключить нейросетевые алгоритмы</h4></p>
  <p><h4>:triangular_flag_on_post: Заменить библиотеку dostoevsky на более лучший анализатор тональности текста</h4></p>
  <p><h4>:triangular_flag_on_post: Улучшить алгоритм работы библиотеки Word2Vec</h4></p>
</div>

---
<div id='description'>
  <p><h3>:microscope:Целью данной работы является совершенствование методов семантического анализа естественно-языкового текста посредством разработки нейросетевой модели распознавания сарказма в тексте.</h3>
  </p>
  <br></br>
  
  <p><h3>Признаковое пространство, используемое для определения сарказма в тексте:</h3></p>
    <p> - Признаки, связанные с частотой. Некоторая неожиданность в тексте может указывать на наличие в тексте сарказма. Одним из индикаторов неожиданности является встречаемость в тексте одновременно как слов с высокой частотой использования, так и слов с низкой частотой;</p>
    <p> - Признаки, связанные со стилем написания. средняя частота слов, написанных в письменном стиле, средняя частота слов, написанных в устном стиле, разница первых двух признаков;</p>
    <p> - Признаки, связанные со структурой предложения. Число глаголов, существительных, прилагательных и наречий; доля глаголов, существительных, наречий и прилагательных в тексте; число всех пунктуационных символов в тексте и др;</p>
    <p> - Признаки, связанные с эмоциональной окраской предложения. Разность между максимальной положительной оценкой и средней, разность между минимальной негативной оценкой и средней;</p>
    <p> - Признаки, связанные с неоднозначностью. Одним из аспектов сарказма является неоднозначность высказывания, которое его содержит;</p>
    <p> - Признаки, связанные с интенсивностью наречий и прилагательных: суммарная интенсивность прилагательных(наречий), средняя интенсивность, максимальная интенсивность</p>
    <br></br>
    
    
  <p><h3>Математическая модель программы:</h3></p>
  <img src='https://user-images.githubusercontent.com/71366294/196294349-176eb4d4-74bd-45fd-b897-24f5b592104e.png' style='width: 880px; height: 600px'/>
  
---
  
  <p><h3>Алгоритм распознавания сарказма:</h3></p>
  <img src="https://user-images.githubusercontent.com/71366294/196293820-407420cd-d50d-40a2-b290-557cf8aeb56d.png"/ style='width: 450px;height: 400px'>
  <p><h4>Основные этапы работы:</h4></p>
  <p>1. Ввод текста, его предобработка и анализ тональности;</p>
  <p>2. Расчёт значений каждого параметра, используемого для распознавания сарказма;</p>
  <p>3. Интегральная оценка полученных параметров и расчет итогового показателя.</p>
  
  ---
  
  <p><h3>Архитектура программного продукта:</h3></p>
  <img src="https://user-images.githubusercontent.com/71366294/196295279-08b129a4-1028-4e3b-8fbc-bc132b98467f.png" />
  
  ---
  <p><h3>Результаты экспериментов</h3></p>
  <img src="https://user-images.githubusercontent.com/71366294/196353663-63b9bec9-f311-41b0-870a-f424ec9ceddf.png" />
  <br></br>
  <img src="https://user-images.githubusercontent.com/71366294/196353868-0748344e-b62e-4c43-83dc-875d3d7d63a2.png"/>
  <br></br>
  <img src="https://user-images.githubusercontent.com/71366294/196353956-e7528cd9-5b3e-4c62-a96a-0764c75f4be6.png"/>
  ---
  
</div>
