# Tema-Internship-ENEA

Sistemul de operare este Ubuntu(last version)
# Instalare si configurare

	1. Python 3 - instalat folosind comanda "apt-get install python3" + update
	
	2. Pentru Selenium am instalat prima data 'pip' apoi cu ajutorul lui am  instalat selenium si restul dependentelor.
		- pip install selenium
		- sudo apt-get install -y unzip openjdk-8-jre-headless xvfb libxi6 libgconf-2-4
		
	3. Programele numpy, opencv si pyautogui au fost usor de instalat si rapid, fiind nevoie doar de o comanda in terminal pentru fiecare
		- pip install numpy
		- sudo apt install python3-opencv
		- pip install pyautogui
		
	4. Pentru pyaudio am intampinat mici dificultati deoarce lipsea un fisier in system (portaudio.h), dar dupa un mic research am descoperit cum il pot instala si am resuit sa adaug si pyaudio.
		- sudo apt-get install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0
		- sudo apt-get install ffmpeg libav-tools
		- sudo pip install pyaudio
	
	5. Pentru a folosi selenium sa accesez browser-ul Chrome ama vut nevoie de o extensie numita "chromium" la care a durat ceva pana sa gasesc comanda corecta pentru a fi adaugat in PATH "chromedriver.exe, in final am reusit sa instalez tot ce aveam nevoie si dupa un mic test am reusit sa deschid o pagina web printr-un script in python utilizand selenium.
		- sudo apt install chromium-browser
	
Dupa instalarea fiecarui program am verificat si ulterior existenta acestuia si versiunea.
In continuare m-am folosit de Visual Studio Code pentru realizarea scripturilor deoarce imi era mai la indemana.

# Realizarea scriptului
Pe parcursul realizarii scriptului am avut nevoie de alte cateva librarii pe care VS Code nu le avea si a necesitat instalarea lor ulterioar (m-am folosit de ‘pip’ si ‘apt-get’).

	1. Incercarea de accesare a www.youtube.com cu selenium a venit cu o eroare deoarece era nevoie sa intalez "tkinter" pentru a mapa mausul in chromium dupa care am accesat cu succes YouTube.

    • Prima problema intampinata dupa ce am accesat Youtube a fost mesajul de tip pop-up pentru cookies, unde trebuia sa selectez butonul de 'Accept' pentur a putea continua navigarea. Dupa putin research am aflat ca ma pot folosi de 'find_element' si limbajul Xpath pentru a spune programului sa apese pe buton, dar imediat ce am accesat sursa  paginii am vazut ca fereastra respectiva este in CSS (javascript), iar Xpath  nu "vede" nimic din aceasta in sursa. Dar am gasit o metoda de a cauta dupa 'CSS_SELECTOR' acel buton si prin adaugarea la final a comenzii 'click()' am resuit sa inchid fereastra.
    
    • De asemenea lipsa unei conexiuni la internet sau pierderea acesteia in timpul rularii ar duce la imposibilitatea finalizarii procesului de navigare, in browser afisandu-se eroarea 'No internet connection' la fel si in terminal.

    • Ulterior am realizat realizat procesul de navigare, indentificarea zonei de search unde am transmis un cuvant dupa care sa se faca cautare, iar cu ajutorul functiei ‘random’ de la 0 pana la numarul de linkuri afisate in pagina am extras unul pe care il va accesa.
	
	2.Inregistrarea ecranului am realizat-o dupa tutorialul din documentatie, am folosit libraria opencv si pyautogui. Rezolutia este preluata automat prin comanda ‘pyautogui.size()', iar pentru a realiza o inregistrare de 2 minute am folosit un for, iteratia facandu-se in functie de FPS-urile alese la crearea functiei de inregistrare. Astfel, de ex pentru a inregistra 2 minute (120 secunde) la 30 FPS for-ul trebuie sa itereze pana la 120 sec * 30 FPS = range(3600).

    • Prima problema intampinata a aparut cand am rulat scriptul deoarece nu inregistra nimic, totul fiind negru. Am constatat ca sursa problemei este de la sistemul de operare, pe partea de 'environment variables' si pachetul 'wayland' din plugin-ul QT. Dupa mai multe incercari esuate si mult research, am reusit sa rezolv problema prin modificarea unor setari din OS. 

    • O a doua problema si pentru care n-am resuit sa gasesc inca o rezolvare era faptul ca 
	dupa finalizarea inregistrarii ecranului, video-ul rezultat ruleaza la o videza mult 	prea mare. 	Am incercat sa ma joc cu FPS-urile crezand ca e de acolo, apoi am adaugat diferite metode 	de sleep/delay in for pe baza a ce am gasit pe internet, dar rezultatul era acelasi de 	fiecare data. Am observat ca pentru valori <10 FPS se misca oarecum mai bine, dar nu la 	viteza 'normala'.
	
    • De asemenea faptul ca utilizez si un monito secundar, programul face captura pe ambele
	si nu am resuit sa gasesc vreo optiune in care sa-i specific de pe ce ecran sa faca 		captura, doar sa redimensionez fereastra de captura si existau sansele ca aceasta sa nu fie in 	aceeasi zona cu locatia browser-ului deschis asa ca am ales sa-l las asa, eventual sa 	deconectez al doilea ecran cand realizez captura de ecran.

    • O problema observata mai tarziu a fost ca timpul de rulare a inregistarii (scriptului) nu trece normal, cu toate ca fisierul avea durata dorita (2 minute). Mai exact scriptul rula mult mai incet in comparatie cu cel de inregistrare audio care mergea exact 2 minute (cronometrat). Problema s-a dovedit a fi de la for care itera greu, astfel ca l-am modificat cu un while in care foloseam libraria ‘time’ sa salvez timpul la care a inceput inregistrarea si cat dureaza aceasta. Astfel cand timpul de start – timpul scurs de rulare ajungea la durata dorita de inregistrare (specificat printr-o variabila) sa se opreasca. Acum scriptul ruleaza normal in concordanta cu cel de inregistrare audio.
	
	3.Inregistrarea audio am realizat-o cu ajutorul tutorialului oferit, folosid ‘pyaudio’. Pentru inceput am facut setarile de baza (canal, frame-uri, rata si durata inregistarii), urmand a fi folosite in procesul de inregistare audio. La fel ca la inregistrarea video, am folosit un for pentru a genera fisierul de durata dorita. Dupa terminarea inregistrarii folosim libraria wave care la randul lui foloseste datele intiale alese pentru a genera fisierul in formatul ‘.wav’.

    • Primul problema sa zic asa pe care am intampinat-o a fost ca nu am stiut la inceput ca acest script foloseste microfonul pentru inregistrare (am presupus ca foloseste iesirea audio) si astfel nu intelegeam de ce nu se aude nimic cand dadeam play la fisieri (micofonul era dat la minim). Ulterior am citit si am aflat acest lucru, dar am incercat sa caut daca exista vreo modalitate de a schimba acest lucru si sa folosesc iesirea audi. M-am documentat mai mult despre ‘pyaudio’ sa vad daca exista posibilitatea sa schimb de unde sa faca inregistrarea, sa folosesc un argument de tip ‘mapping’ si sa selectez canalul folosit, dar rezultatul nu a fost cel asteptat. Astfel ca dupa modificarea scriptului pe langa cateva erori pe care am resuit sa le rezolv dupa multe incercari, inregistrarea nu putea fi accesata, imi dadea eroare cand o deschideam (am incercat cu mai multe programe).

    • Cum microfonul laptopului este destul de slab ca si performanta, pe inregistrare se aud si alte ‘zgomote’ pe langa ce ar trebui sa inregistreze, rezultatul nefiind foarte calitativ. Pentru a avea o inregistrare cat mai buna ar trebui sa folosesc un microfon extern, eventual unul care sa anuleze aceste zgomote de fundal pentru o procesare cat mai calitativa a sunetului.  

	4. Extragerea nivelului sunetului in decibeli din fisierul audi o fac cu ajutorul librariei ‘scipy’ de la care folosesc ‘wavfile’ cu ajutorul careia extrag din fisier rata si matricea de date. Pe langa aceasta mai folosesc si libraria ‘audioop’ prin extrag puterea semnalului audio (pe baza datelor din matricea de date) asupra careia aplic formula matematica 20log(10)*(valoare), obtinand astfel valoarea in decibeli a sunetului pe care-l salvez intr-un fisier.
	
	 • Varianta aceasta nu a fost prima abordata in incercarea de extragere valoarea sunetului in decibeli. Prima a fost folosirea unei formule matematici putin mai complexa aplicata fara a mai folosi 'audioop' doar 'wavfile', iar formula gasita intr-o documentatie despre procesarea sunetului din fisiere '.wav' era '20log10(sqrt(abs(valoare^2)))', dar am observat ca valorile returnate erau gresite intre [10, 30] dB (valorile normale ar fi >50dB) si multe falori de tip 'nan' 
	
	5. Pentru combinarea inregistrarilor audi/video folosesc libraria 'ffmpeg' care imi permite doar printr-o simpla linie de comanda trimisa in terminal sa obtin fisierul video cu audio integrat. 
	
	 • Singura problema ce ar putea sa apara la rularea comenzii ar fi lipsa unuia dintre fisiere sau a ambelor si existenta deja a fisierului final, comanda neavand posibilitatea de a-l suprascrie. 
