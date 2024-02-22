#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include <ctype.h>

struct Tempo{
   char hora[7] ;

};

struct cad_carro{
     char placa[8], modelo[20], marca[20], cor[10];
     int status;
     struct Tempo entrada;


}carro[10];

int nvei=0; //contador de ve�culos cadastrados
char pesq[8];

void inicializa()
{
     int i;

     for(i=0; i<10; i++)
     carro[i].status=0;
}

//verifica placa
int verifica_placa(int n){
    if (n==0){
        return 0;
	}
	else{
        return 1;
	}
}
// verifica se o estacionamento esta vazio
int verifica(int n)
{
	if (n==0){
        return 0;
	}
	else{
        return 1;
	}
}

//limpa do registro o carro que saiu do estacionamento
void excluir(int i)
{
     carro[i].placa==0;
     carro[i].modelo==0;
     carro[i].marca==0;
     carro[i].cor==0;
     carro[i].entrada.hora==0;
     carro[i].status==0;
}
//inserir dados dos veiculos
void inserir(int i)
{
   char pla[8];
   int j, teste, tam_pla,r;
   FILE *P;

      puts("Digite a placa: ");
      fflush(stdin);
      gets(pla);

      strupr(pla);//deixa caracteres da placa em CAIXA ALTA

      strcpy(carro[i].placa, pla);

      tam_pla=strlen(carro[i].placa);
      // Testa quantos digitos foram inseridos, minimo 7
      if(tam_pla!=7)
      {
        if(tam_pla<7)
        {
        printf("\nPlaca invalida\nDigitos insuficientes\n\n");
        inserir(i);
        }
        else//(tam_pla>7)
        {
        printf("\nPlaca invalida\nMuitos digitos\n\n");
        inserir(i);
        }
      }
       //testa se 3 primeiros digitos é letra
       for(j=0; j<3; j++)
       {
          teste=isalpha(carro[i].placa[j]);//retorna 1 se for letra
          r==verifica_placa(teste);
          if(r==1)
          {
          printf("\nPlaca invalida\nTres primeiros digitos devem ser letras!\n\n");
          inserir(i);
          }
       }

      //testa se 4 ultimos digitos nao sao letras
      for(j=3; j<7; j++)
      {
            teste=isalpha(carro[i].placa[j]);//retorna 1 se for letra
            r==verifica_placa(teste);
            if(teste==1)
            {
            printf("\nPlaca invalida\nQuatro ultimos digitos devem ser numeros!\n\n");
            inserir(i);
            }
      }

   puts("\nDigite o modelo: ");
   fflush(stdin);
   gets(carro[i].modelo);
   strlwr(carro[i].modelo);
   carro[i].modelo[0]=toupper(carro[i].modelo[0]);

   puts("\nDigite a marca: ");
   fflush(stdin);
   gets(carro[i].marca);
   strlwr(carro[i].marca);
   carro[i].marca[0]=toupper(carro[i].marca[0]);

   puts("\nDigite a cor: ");
   fflush(stdin);
   gets(carro[i].cor);
   strlwr(carro[i].cor);
   carro[i].cor[0]=toupper(carro[i].cor[0]);

   puts("\nDigite a hora da entrada no formato <horas>:<minutos>:(digitar os :)");
   gets(carro[i].entrada.hora);
   carro[i].status=1;

   P=fopen("CARRO.txt", "w");
   fwrite(&carro, sizeof(carro), 1, P);
   fclose(P);
}
//----------------------------------------------------------
//cadastrar a entrada de veiculos 
void cadastrar_veiculo(){
     int i, flag=1;

     for(i=0; i<10; i++)
     {
        if(carro[i].status==0)
        {
        inserir(i);
        printf("\n\nVeiculo cadastrado com sucesso!");
        flag=0;
        break;
        }
     }

     if(flag==1)
     {
     printf("Sem espaco para cadastrar\nEnter para voltar ao menu...");
     getchar();
     }
}
// Procedimento para registrar a saida e calcular o valor a ser pago
void saida_veiculo(){
	FILE *P;
	P=fopen("CARRO.txt", "r");
    fread(&carro, sizeof(carro), 1, P);
     int i;
	 int horaEnt,minEnt,horaSai, minSai,tminEnt,tminSai,T_total;
	 float precoad=0.50;// valor por minuto adicional acima de 1hora
     float preco=10.00;//valor por utilizacao de ate 1h

    puts("Digite a placa: ");
      fflush(stdin);
      gets(pesq);
    strupr(pesq);
            for(i=0;i<10;i++){
                 if(strcmp(pesq,carro[i].placa)==0){
             printf("\n Placa: %s", carro[i].placa);
             printf("\n Modelo: %s", carro[i].modelo);
             printf("\n Marca: %s", carro[i].marca);
             printf("\n Cor: %s", carro[i].cor);
             printf("\n Hora de Entrada: %s\n\n", carro[i].entrada.hora);
             carro[i].status=0;
             excluir(i);

            printf("\n\n Digite a hora de entrada no formato <horas>enter<minutos>:\n");
            scanf("%d""%d",&horaEnt,&minEnt);
            printf("\n\n\n Digite a hora de saida no formato <horas>enter<minutos>:\n");
            scanf("%d""%d", &horaSai, &minSai);
            tminEnt = (horaEnt*60)+ minEnt;
            tminSai = (horaSai*60)+ minSai;
            T_total = tminSai-tminEnt; //calcula o tempo total
            //Informa o valor para estacionar at� a dura��o de 1h.Valor RS1,00 pela primeira hora
            if(T_total<=60){
            	printf("O carro do cliente ficou %d minutos no estacionamento, e o valor total a pagar e de: R$%.2f ",T_total, preco);
			}
			else{
			       float valorapagar = ((T_total-60)*precoad) + preco;// Calcula o valor da primeira hora mais o valor dos minutos adicionais. depois de 1h cada minuto adicional custa R$ 0.05

			    printf("O carro do cliente ficou %.d minutos no estacionamento, e o valor total a pagar � de: R$%.2f\n\n\n",T_total, valorapagar);

            }

			P=fopen("CARRO.txt", "w");
            fwrite(&carro, sizeof(carro), 1, P);
            fclose(P);
             }
             if (i==10){
                     printf("Veiculo nao encontrado");
             }
             }

}
// Procedimento para listar os veiculos que estao no estacionamento.
void listar_veiculo()
{
    int i,j, n=1, r;

    FILE *P;
    fread(&carro, sizeof(carro), 1, P);

    for(i=0; i<10; i++)
    {
   	if(carro[i].status==1)
   	  {
      printf("Veiculo %d\nPlaca: %s\t Modelo: %s\t Marca: %s\t Cor: %s\n\n", i+1, carro[i].placa, carro[i].modelo, carro[i].marca, carro[i].cor);
      printf("Entrada: %s\n\n\n\n", carro[i].entrada.hora);
	  n=0;
      }
    }
    r=verifica(n);
    if(r==0)
    {
    printf("\nEnter voltar ao menu...");
    getchar();
    }
    else
    {
   	puts("Nenhum veiculo cadastrado\nEnter voltar ao menu...");
   	getchar();
    }
}
//-----------------------------------------------------------------------------

int main()
{
    int opcao;
      FILE* P;

      inicializa();

		printf("-------------------------------------------");

      do{
      printf("\nCONTROLE DE ESTACIONAMENTO\n\n");
      printf("-------------------------------------------\n\n");
      printf("1. Cadastrar entrada de veiculo\n");
      printf("2. Informar saida do veiculo \n3. Listar veiculos\n4. Sair\n\nOpcao: ");
      scanf("%d", &opcao);

               switch(opcao)
               {
                    case 1:
                    {
                    cadastrar_veiculo();
                    break;
                    }
                    case 2:
                    {
                    saida_veiculo();
                    break;
                    }
                    case 3:
                    {
                    listar_veiculo();
                    break;
                    }
					case 4: break;
                    default:
                    {
                    printf("Opcao invalida!\nEnter para voltar ao menu");
                    getchar();
                    }
               }
        }while(opcao!=4);
      getchar();
  return 0; 
}