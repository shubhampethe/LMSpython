#include <stdio.h>
#include <string.h>
int main()
{
  char name[20];
  int rno, math, dmath, data, graphics, micro, python, en, isemath, isedmath, isedata, isegraphics, isemicro, isepython, pdata;
  int imath, idmath, idata, igraphics, imicro, ipython, mtotal, dmtotal, dtotal, ctotal, mitotal, ptotal, total, percentage;
  char fail[5];
  printf("\n Please enter your name:");
  scanf("%[^\n]*c", name);
  printf("\n Please enter your roll number:");
  scanf("%d", &rno);
g:
  printf("\n Please enter your thoery marks of Applied Mathematics-I:");
  scanf("%d", &math);
  if (math < 0 || math > 70)
  {
    printf("\n Please reenter your correct marks:");
    goto g;
  }
g1:
  printf("\n Please enter your ISE marks of Applied Mathematics-I:");
  scanf("%d", &isemath);
  if (isemath < 0 || isemath > 30)
  {
    printf("\n Please reenter your correct marks:");
    goto g1;
  }
g2:
  printf("\n Please enter your internal marks of Applied Mathematics-I:");
  scanf("%d", &imath);
  if (imath < 0 || imath > 25)
  {
    printf("\n Please reenter your correct marks:");
    goto g2;
  }
  mtotal = math + isemath + imath;
g3:
  printf("\n Please enter your theory marks of Discret Mathematical Structures:");
  scanf("%d", &dmath);
  if (dmath < 0 || dmath > 70)
  {
    printf("\n Please reenter your correct marks:");
    goto g3;
  }
g4:
  printf("\n Please enter your ISE marks of Discret Mathematical Structures:");
  scanf("%d", &isedmath);
  if (isedmath < 0 || isedmath > 30)
  {
    printf("\n Please reenter your correct marks:");
    goto g4;
  }
g5:
  printf("\n Please enter your internal marks of Discret Mathematical Structures:");
  scanf("%d", &idmath);
  if (idmath < 0 || idmath > 25)
  {
    printf("\n Please reenter your correct marks:");
    goto g5;
  }
  dmtotal = dmath + isedmath + idmath;
g6:
  printf("\n Please enter your theory marks of Data structures:");
  scanf("%d", &data);
  if (data < 0 || data > 70)
  {
    printf("\n Please reenter your correct marks:");
    goto g6;
  }
g7:
  printf("\n Please enter your practical marks of Data structures:");
  scanf("%d", &pdata);
  if (pdata < 0 || pdata > 50)
  {
    printf("\n Please reenter your correct marks:");
    goto g7;
  }
g19:
  printf("\n Please enter your ISE marks of Data structures:");
  scanf("%d", &isedata);
  if (isedata < 0 || isedata > 50)
  {
    printf("\n Please reenter your correct marks:");
    goto g19;
  }
g8:
  printf("\n Please enter your internal marks of Data structures:");
  scanf("%d", &idata);
  if (idata < 0 || idata > 25)
  {
    printf("\n Please reenter your correct marks:");
    goto g8;
  }
  dtotal = data + pdata + isedata + idata;
g9:
  printf("\n Please enter your theory marks of Computer grapgraphics:");
  scanf("%d", &graphics);
  if (graphics < 0 || graphics > 70)
  {
    printf("\n Please reenter your correct marks:");
    goto g9;
  }
g10:
  printf("\n Please enter your ISE marks of Computer grapgraphics:");
  scanf("%d", &isegraphics);
  if (isegraphics < 0 || isegraphics > 30)
  {
    printf("\n Please reenter your correct marks:");
    goto g10;
  }
g11:
  printf("\n Please enter your internal marks of Computer grapgraphics:");
  scanf("%d", &igraphics);
  if (igraphics < 0 || igraphics > 25)
  {
    printf("\n Please reenter your correct marks:");
    goto g11;
  }
  ctotal = graphics + isegraphics + igraphics;
g12:
  printf("\n Please enter your thoery marks of Microprocessors:");
  scanf("%d", &micro);
  if (micro < 0 || micro > 70)
  {
    printf("\n Please reenter your correct marks:");
    goto g12;
  }
g13:
  printf("\n Please enter your ISE marks of Microprocessors:");
  scanf("%d", &isemicro);
  if (isemicro < 0 || isemicro > 30)
  {
    printf("\n Please reenter your correct marks:");
    goto g13;
  }
g14:
  printf("\n Please enter your internal marks of Microprocessors:");
  scanf("%d", &imicro);
  if (imicro < 0 || imicro > 25)
  {
    printf("\n Please reenter your correct marks:");
    goto g14;
  }
  mitotal = micro + isemicro + imicro;
g15:
  printf("\n Please enter your practical marks of Python Pogramming:");
  scanf("%d", &python);
  if (python < 0 || python > 50)
  {
    printf("\n Please reenter your correct marks:");
    goto g15;
  }
g16:
  printf("\n Please enter your ISE marks of Python Pogramming:");
  scanf("%d", &isepython);
  if (isepython < 0 || isepython > 30)
  {
    printf("\n Please reenter your correct marks:");
    goto g16;
  }
g17:
  printf("\n Please enter your internal marks of Python Pogramming:");
  scanf("%d", &ipython);
  if (ipython < 0 || ipython > 25)
  {
    printf("\n Please reenter your correct marks:");
    goto g17;
  }
  ptotal = python + isepython + ipython;
g18:
  printf("\n Please enter your marks of Environmental studies:");
  scanf("%d", &en);
  if (en < 0 || en > 50)
  {
    printf("\n Please reenter your correct marks:");
    goto g18;
  }
  printf("\n               \t\tYOUR SEMISTER-III RESULT");
  printf("\n |------------------------------------------------------------------------------------------------------------------------------------");
  printf("\n |");
  printf("\n |             \t\tBRANCH:CSE");
  printf("\n |");
  printf("\n |------------------------------------------------------------------------------------------------------------------------------------");
  printf("\n |NAME: %s", name);
  printf("\n |ROLL NO: %d", rno);
  printf("\n |");
  printf("\n |------------------------------------------------------------------------------------------------------------------------------------");
  if (math < 27 || dmath < 27 || data < 27 || graphics < 27 || micro < 27 || en < 17 || python < 17)
  {
    if (isemath < 11 || isedmath < 11 || isedata < 11 || isegraphics < 11 || isemicro < 11)
    {
      printf("\n |STATUS:FAIL");
    }
  }
  else
  {
    printf("\n |STATUS:PASS");
  }
  printf("\n |------------------------------------------------------------------------------------------------------------------------------------");
  printf("\n |");
  printf("\n |Subject marks\t\t\t\tMarks\t\tPractical marks\t\tISE marks\t\tInternal marks\t\tTotal");
  printf("\n |");
  printf("\n |------------------------------------------------------------------------------------------------------------------------------------");
  printf("\n |Applied Mathematics-I:   \t\t%d\t\t-\t\t\t%d\t\t\t\t%d\t\t  %d", math, isemath, imath, mtotal);
  printf("\n |Discret Mathematical Structures:\t%d\t\t-\t\t\t%d\t\t\t\t%d\t\t %d", dmath, isedmath, idmath, dmtotal);
  printf("\n |Data structures:\t\t\t%d\t\t%d\t\t\t%d\t\t\t\t%d\t\t %d", data, pdata, isedata, idata, dtotal);
  printf("\n |Computer grapgraphics:    \t\t%d\t\t-\t\t\t%d\t\t\t\t%d\t\t %d", graphics, isegraphics, igraphics, ctotal);
  printf("\n |Microprocessors:\t\t\t%d\t\t-\t\t\t%d\t\t\t\t%d\t\t%d", micro, isemicro, imicro, mitotal);
  printf("\n |Python Pogramming:       \t\t-\t\t%d\t\t\t%d\t\t\t\t%d\t\t %d", python, isepython, ipython, ptotal);
  printf("\n |Environmental studies:    \t\t%d\t\t-\t\t\t-\t\t\t\t-\t\t %d", en, en);
  printf("\n |------------------------------------------------------------------------------------------------------------------------------------");
  printf("\n |");
  total = mtotal + dmtotal + dtotal + ctotal + mitotal + ptotal + en;
  printf("\n |\t\t\t\t\tTOTAL:%d", total);
  percentage = total / 7.75;
  printf("\n |");
  printf("\n |percentage:%d", percentage);
  printf("\n |------------------------------------------------------------------------------------------------------------------------------------");
  return 0;
}