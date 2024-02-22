#include <stdio.h>
#include <conio.h>

  enum mes {Janeiro = 1, Fevereiro, Marco, Abril, Maio, Junho,
  Julho, Agosto, Setembro, Outubro, Novembro, Dezembro}meses;
int main(void) {

  printf("Digite o numero do mes: ");
  scanf("%d",&meses);
  
  //Testando se o valor está na faixa válida 
  if((meses >= Janeiro) && (meses <= Dezembro)) {
    //switch que determina o mes impresso
    switch(meses) {

    case Janeiro:
    printf("%d - Janeiro",meses);
    break;
    
    case Fevereiro:
    printf("%d - Fevereiro",meses);
    break;
    
    case Marco:
    printf("%d - Marco",meses);
    break;
    
    case Abril:
    printf("%d - Abril",meses);
    break;
    
    case Maio:
    printf("%d - Maio",meses);
    break;
    
    case Junho:
    printf("%d - Junho",meses);
    break;
    
    case Julho:
    printf("%d - Julho",meses);
    break;
    
    case Agosto:
    printf("%d - Agosto",meses);
    break;
    
    case Setembro:
    printf("%d - Setembro",meses);
    break;
    
    case Outubro:
    printf("%d - Outubro",meses);
    break;
    
    case Novembro:
    printf("%d - Novembro",meses);
    break;
    
    case Dezembro:
    printf("%d - Dezembro",meses);
    break;
    
    }
  }
  else { //senão estiver na faixa válida exibe mensagem
    printf("Valor INVALIDO!!!\n");
    
    printf("Os valores validos para os meses do ano sao: \n\n");

    //Loop que exibe a faixa de valores válida
    //Como os valores de enum são inteiros, podem ser implementados em um loop
    
    for(meses = Janeiro; meses <= Dezembro; meses++)
      printf("Mes: %d \n",meses);
  }
  
  getch();
  return 0;
}