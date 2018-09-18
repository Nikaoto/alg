# მონაცემთა სტრუქტურები და ალგორითმები
ეს რეპოზიტორი არის ჩემი მონაცემთა სტრუქტურებისა და ალგორითმების დავალებების 
თავმოყრის ადგილი

### ფაილების სტრუქტურა
ყოველი ფაილი შეესაბამება დავალებას რიგითობის მიხედვით. `01` - პირველი, `07` - მეშვიდე, 
`23` - ოცდამესამე...

დავალების ქვეპუნქტებიც იგივე გზით აღინიშნება. `01/01` - პირველი დავალების პირველი 
ქვეპუნქტი, `03/11` - მესამე დავალების მეთერთმეტე ქვეპუნქტი. 


ასეთი სტრუქტურა ავარჩიე, რადგან თითოეული დავალება მარტივად წასაკითხი და იზოლირებული 
იყოს ყველაფრისგან. ყველა რესურსი და დამატებითი სორს ფაილები შეეხება მხოლოდ ერთ 
კონკრეტულ სავარჯიშოს.

### ფორმატი
თითოეულ სორს ფაილს თავში გააჩნია მოკლე აღწერა კომენტარის სახით. მისი შემადგენელი 
ნაწილებია: 
* ავტორის სახელი და გვარი
* დავალების ნომერი
* კოდის დანიშნულება

მაგალითად:
```c
/* 
  ნიკოლოზ ოთიაშვილი, დავალება 3.4;
  ბეჭდავს ფიბონაჩის მიმდევრობიდან პირველ 47 რიცხვს
*/

 #include <stdio.h>

 int main() {
   int n = 47, curr = 0, temp, next;
   for (int i = 0; i < n; i++) {
     printf("%d\n", curr);
     next = curr + temp;
     curr = temp;
     temp = next;
   }
   return 0;
 }
```

არ ვიცი ინგლისურად ჯობს კომენტარების წერა თუ ქართულად. შეიძლება ეგ შევცვალო.

## მნიშვნელოვანი ფაილები
*კონკრეტული კოდის მარტივად მიგნებისთვის ლინკების ჩამონათვალი*

- წრფივი ძებნა მასივში - [01/search.py](01/search.py)
