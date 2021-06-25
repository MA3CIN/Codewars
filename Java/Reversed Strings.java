public class Kata {

  public static String solution(String str) {
    char arr[] = str.toCharArray();
    String wynik = "";
    for (int i = arr.length-1; i>-1; i--){
      wynik += arr[i];
    }
    return wynik;
  }

}