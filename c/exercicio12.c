#include <stdio.h>
#include <stdlib.h>

int main(){
	system("chcp 65001"); 
	
	int horas_mes;
	float valor_hora, salario_liquido, salario_bruto, desconto;
	
	printf("Quantas horas você trabalha no mês? ");
	scanf("%d", &horas_mes);
	printf("Quantos reais você ganha por hora?");
	scanf("%f", &valor_hora);
	
	salario_bruto = horas_mes * valor_hora;
	desconto = (salario_bruto * 9) / 100;
	salario_liquido = salario_bruto - desconto;
	
	printf("Você ganha um salário bruto de %.2f\n", salario_bruto);
	printf("Com o desconto de 9% do INSS, o seu salário líquido é de %.2f", salario_liquido);
	
	return 0;
}
