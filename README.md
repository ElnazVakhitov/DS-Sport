# DS-Sport

Это мой проект анализа данных в спорте, а именно в футболе. На данный момент работа(возможно) идет до сих пор, поэтому этот репозиторий еще будет обновляться.

## Colab
* [Попытка TS рейтинга / неудачно](https://colab.research.google.com/drive/1-YiYDcnRvrty_m4tp1VvR_Dm5I4iTD7K)
* [Попытка предикта рейтинга / неудачно](https://colab.research.google.com/drive/1boAIhldxgZE3sHBRcjSM_1rcjGbA1wSg)
* [Предикт падения команды(чтобы это не значило) / успешно](https://colab.research.google.com/drive/1tORdStkegL9ph9oD8G8QHoHOLiJyl9cb?usp=sharing)
* [Предкит эффективности матча / успешно](https://colab.research.google.com/drive/1uG7Owh04-pYmkwOr2Vnra90Eov6wGZj_?usp=sharing)

Данные брались с сайта [https://www.flashscorekz.com/?rd=flashscore.ru.com].

Сейчас идет подсчет забитых/пропущенных голов, в данных испльзуется еще алгоритм СЛУ по прошлым счетам в команде(который в excel таблицы), но в будущем планируется избавиться от него.

* [Текущие итоги](https://colab.research.google.com/drive/1uG7Owh04-pYmkwOr2Vnra90Eov6wGZj_#scrollTo=u22j1oDP6ozC&uniqifier=2)


По итогу добился MAE = 0.8 по предикту забитых/пропущенных голов. Я уверен, в том что можно добиться и лучшего результата, хорошо просемплировав данные и добавив возможно новые фичи. 

Я конечно понимаю, что тут все без оформления и выглядит кринжово, но что есть, то есть
