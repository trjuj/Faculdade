#include <stdlib.h>
#include <stdio.h>
#include <math.h>

int main (void){

	/*	int=
		caso = case referente cadeira
		i = fileiras das cadeiras
		j = colunas das cadeiras
		lin = linha escolhida 
		col = coluna escolhida 

		char=
		asctr = referente ao caractere "-"
		asci = referente ao caractere "i"
		ascm = referente ao caractere "m"
		poltrona[14] [10] = referente a matriz das cadeiras
	*/
	
	int caso, i, j, lin, col, n, t, x, p, q, CONint = 0, CONmei = 0;
	int cinema[14][10];
	char asctr = 45; // -
	char asci = 105; // i
	char ascm = 109; // m

	for(i=0 ; i<14; i++)
	{
		for(j=0 ; j<10 ; j++)
		{
			cinema[i][j]=0;
		}
	}
	do
	{			
			printf("\n[0] - CANCELA\n");
			printf("[1] - Escolher Cadeira\n");
			printf("[2] - Ver cadeiras disponiveis\n");
			scanf("%d", &caso);
			
			switch(caso)
			{	
				case 1: //Escolher Cadeira
					printf("Inteira [1] ou Meia [2]: ");
					scanf("%d", &q);
					if ((q!=1)&&(q!=2)){
						printf("Opcao invalida\n");
					}else{
					printf("Fila: ");
					scanf("%d", &lin);
					printf("Coluna: ");
					scanf("%d",&col);
					if (lin<14 && col<10)
					{
						if (cinema[lin][col]==0)
						{
							if (q==1){
								cinema[lin][col]=1;
							}if (q==2){
								cinema[lin][col]=2;
							}
						}
						else
						{
							printf("CADEIRA OCUPADA\n\n");
						}
					}
					else
					{
						printf("A CADEIRA SELECIONADA NAO EXISTE");
					}
					printf("\n");}
					break;
				case 2: //ver caideiras
					n=0;
					printf("\n--- Disponibilidade na sala ---\n\n");
					printf("\tC\n\tO\n\tL\n\tU\n\tN\n\tA\n");
					printf("LINHA");
					printf("\t   0 1 2 3 4 5 6 7 8 9\n");
							for(i=0 ; i<14; i++){
									printf("\t");
									n==2;
									if (n>=10){
										printf("%d ",n);
									}else{
										printf("%d  ",n);
									}
									n++;
								
								for(j=0 ; j<10 ; j++)
								{
									if(cinema[i][j]==1)
									{
										printf("%c ",asci);
										CONint++;
									}
									if(cinema[i][j]==2)
									{
										printf("%c ",ascm);
										CONmei++;
									}
									if((cinema[i][j]!=1)&&(cinema[i][j]!=2))
									{
										printf("%c ",asctr);
									}
								}
								
							printf("\n");
					}
					printf("Numero de lugares ocupados: %d\n", CONmei+CONint);
					printf("Meia entrada: %d\nEntrada inteira: %d\n", CONmei,CONint);
					break;	
			}
		
	}while(caso!=0);
	printf("Obrigado por usar o programa!");
	return(0);
}