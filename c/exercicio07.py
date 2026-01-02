#include <stdio.h>
#include <stdlib.h>
int main(){
	float vm, d, litros, t;
	
	printf("Qual foi o tempo de viagem em horas?\n");
	scanf("%f", &t);
	printf("Qual foi a velocidade media da viagem em Km/h?\n");
	scanf("%f", &vm);
	
	d = t * vm;
	litros = d / 12;
	
	printf("Dados da sua viagem: \n");
	printf("Tempo gasto: %.2f horas \n", t);
	printf("Velocidade media: %.2f Km/h \n", vm);
	printf("Distancia percorrida: %.2f Km \n", d);
	printf("Quantidade de gasolina usada: %.2f litros\n", litros);
	
	return 0;
}
