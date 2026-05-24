int dots[6] = {2,3,4,5,6,7};

void setup()
{
  Serial.begin(9600);

  for(int i=0;i<6;i++)
  {
    pinMode(dots[i], OUTPUT);
    digitalWrite(dots[i], LOW);
  }
}

void clearDots()
{
  for(int i=0;i<6;i++)
  {
    digitalWrite(dots[i], LOW);
  }
}

void showPattern(String pattern)
{
  clearDots();

  for(int i=0;i<6;i++)
  {
    if(pattern[i] == '1')
    {
      digitalWrite(dots[i], HIGH);
    }
  }

  delay(800);
  clearDots();
}

void loop()
{
  if(Serial.available())
  {
    String pattern = Serial.readStringUntil('\n');
    pattern.trim();

    if(pattern.length() == 6)
    {
      showPattern(pattern);
    }
  }
}