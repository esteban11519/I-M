%% imports data from audacity and experimental dice data 
clear
clc
close
load("/home/daniel/Desktop/I&M/pr3Datos.mat");
%% 1.
close 
selectFig=[1 1 1]; %selects which figures you want [histogram temporalSec unitDelay];
showEm(datosUnDado, datosDosDados, 50, selectFig); %function below to show everything

clear selectFig
%% 2&3 
clc
close
repe=[10 20 30 50 100 1000]; %repe is the vector with repetitions per experiment
whichFig=[1 0 0];  %selects which figures you want [histogram temporalSec unitDelay];
for i=1:length(repe)
    unD=rollDices(1, 6, repe(i));
    dosDR=rollDices(2, 6, repe(i));
    showEm(unD, dosDR, repe(i), whichFig);
end

clear whichFig repe 
%% 4. 
clc
close
repe=[10 20 30 50 100 1000];%repe is the vector with repetitions per experiment
selectFig=[1 0 0]; %selects which figures you want [histogram temporalSec unitDelay];
for i=1:length(repe)
    dataNow=dataAudacity(1:repe(i));
    showAuda(dataNow, repe(i), selectFig, fs);
end

clear repe slectFig
%% 5. 
clc
close
selectFig=[1 0 0]; 
showMoney(mon2SellData, 30, selectFig,2);
showMoney(mon3SellData, 30, selectFig,3);

mon2SellDataMil=randi([0 2], 2, 1000);
mon3SellDataMil=randi([0 3], 3, 1000);

showMoney(mon2SellDataMil, 1000, selectFig,2);
showMoney(mon3SellDataMil, 1000, selectFig,3);

clear selectFig 
%% Para calcular número de clases se puede usar esta aproximación 
% en la función showAuda se aplica esta fórmula
%n= número de muestras 
%k aprox= 1+ 3.3 log( n ) 
%clases = intervalo / k 

%% Functions
function v=rollDices(number, faces, rep)
    vini=randi(faces, number, rep);
    v=1:rep;
    for i=1:rep 
        v(i)=sum(vini(:,i));
    end
end

function showEm(uno, dos, num, boole)
    %% Histograms
    if (boole(1))
        figure
        subplot(2,1,1);
        C=categorical(uno);
        histogram(C);
        ylabel("Repeticiones");
        xlabel("Valor del lanzamiento");
        title("Histograma para un dado, " + num + " lanzamientos" );
        grid on
        subplot(2,1,2);
        C=categorical(dos);
        histogram(C);
        ylabel("Repeticiones");
        xlabel("Valor del lanzamiento");
        title("Histograma para dos dados, " + num + " lanzamientos" );
        grid on
    end
    %% Temporal sequence 
    if(boole(2))
        figure
        subplot(2,1,1);
        plot(uno, 'o');
        ylabel("Valor del lanzamiento");
        xlabel("Número de lanzamiento");
        title("Secuencia temporal para un dado, " + num + " lanzamientos" );
        %grid on
        subplot(2,1,2);
        plot(dos,'o');
        ylabel("Valor del lanzamiento");
        xlabel("Número de lanzamiento");
        title("Secuencia temporal para dos dados, " + num + " lanzamientos" );
        %grid on
    end
    %% Retardo unitario
    if(boole(3))
        figure
        subplot(2,1,1);
        unom=[uno(2:num) uno(1)];
        plot(unom, uno, 'o');
        ylabel("Valor del lanzamiento actual");
        xlabel("Valor de lanzamiento anterior");
        title("Diagrama de retardo unitario para un dado, " + num + " lanzamientos" );
        %grid on
        subplot(2,1,2);
        dosm=[dos(2:num) dos(1)];
        plot(dosm, dos, 'o');
        ylabel("Valor del lanzamiento actual");
        xlabel("Valor de lanzamiento anterior");
        title("Diagrama de retardo unitario para dos dados, " + num + " lanzamientos" );
        %grid on
    end
end

function showAuda(data, num, boole, freq)
    %% Histograms
    if (boole(1))
        k=1+3.33 * log(num);
        figure
        histogram(data, fix(k));%fix is for making it integer
        ylabel("Repetición dato");
        xlabel("Valor de audio");
        title("Histograma para audio, " + num + " muestras" );
        grid on
    end
    %% Temporal sequence 
    if(boole(2))
        figure
        time=1:length(data);
        time=time.*1/freq;
        plot(time, data, 'o');
        ylabel("Valor de la señal");
        xlabel("Tiempo (S)");
        title("Secuencia temporal para el audio, " + num + " muestras" );
    end
    %% Retardo unitario
    if(boole(3))
        figure
        datam=[data(2:num) data(1)];
        plot(datam, data, 'o');
        ylabel("Valor de señal tiempo actual");
        xlabel("Valor de señal tiempo anterior");
        title("Diagrama de retardo unitario para señal de audio, " + num + " muestras" );
        
    end
end

function showMoney(data, num, boole, cuantas)
    %% Histograms
    if (boole(1))
        figure
        C=categorical(data);
        histogram(C);
        ylabel("Repeticiones en experimento");
        xlabel("Número de sellos en lanzamiento");
        title("Histograma para "+cuantas+" monedas, " + num + " lanzamientos" );
        grid on
    end
    %% Temporal sequence 
    if(boole(2))
        figure
        plot(data, 'o');
        ylabel("Número de sellos en lanzamiento");
        xlabel("Número de repetición");
        title("Secuencia temporal para "+cuantas+" monedas, " + num + " muestras" );
    end
    %% Retardo unitario
    if(boole(3))
        figure
        datam=[data(2:num) data(1)];
        plot(datam, data, 'o');
        xlabel("Cantidad de sellos repetición anterior");
        ylabel("Cantidad de sellos repetición actual");
        title("Diagrama de retardo unitario experimento con " +cuantas+" monedas, " + num + " muestras" );
        
    end
end