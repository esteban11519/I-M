%% 1 
num=5000;
unD=randi(6, num, 1);
dosD=randi(6, num, 2);
dosDR=1:num;
for i=1:num 
    dosDR(i)=sum(dosD(i,:));
end

%% a 
figure
subplot(2,1,1);
histogram(unD);
ylabel("Repeticiones");
xlabel("Valor del lanzamiento");
title("Histograma para un dado, " + num + " lanzamientos" );
grid on
subplot(2,1,2);
histogram(dosDR);
ylabel("Repeticiones");
xlabel("Valor del lanzamiento");
title("Histograma para dos dados, " + num + " lanzamientos" );
grid on
%%  b
figure
subplot(2,1,1);
plot(unD);
ylabel("Valor de lanzamiento");
xlabel("Lanzamiento");
title("Secuencia temporal para un dado, " + num + " lanzamientos" );
grid on
subplot(2,1,2);
plot(dosDR);
ylabel("Valor de lanzamiento");
xlabel("Lanzamiento");
title("Secuencia temporal para dos dados, " + num + " lanzamientos" );
grid on


