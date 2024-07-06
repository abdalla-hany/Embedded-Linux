/**
 * @file functions.cpp
 * @author Abdalla Hany (abdallahanyalsaid77@gmail.com)
 * @brief main source file for all functions used in HMI screen
 * @version 0.1
 * @date 2024-07-04
 *
 * @copyright Copyright (c) 2024
 *
 */

#include "hmi_functions.h" /* HMI function prototypes */
#include "keypad.h"        /* Keypad input functions */
#include "lcd.h"           /* LCD control functions */
#include "std_types.h"     /* Standard data types */
#include "timer1.h"        /* Timer1 control functions */
#include "uart.h"          /* UART communication functions */
#include <avr/io.h>        /* For AVR device-specific IO definitions (SREG) */
#include <util/delay.h>    /* For the delay functions */

/*******************************************************************************
 *                          Global Variables                                   *
 *******************************************************************************/

/* Global variables for password storage and attempt tracking */
uint8 g_firstPass[PASSWORD_SIZE] = {0};
uint8 g_secondPass[PASSWORD_SIZE] = {0};
uint8 g_attempt = 0, g_seconds = 0;

/*******************************************************************************
 *                      Functions  Definitions                                 *
 *******************************************************************************/

/**
 * @brief Function to initialize HMI components
 *
 * @param void
 *
 * @return void
 */
void Init_Function(void) {
  /* UART configuration structure */
  UART_ConfigType uart = {EVEN_PARITY, ONE_STOP_BIT, EIGHT_BIT, 9600};

  /* Initialize UART, LCD, and Timer1 with callback function */
  UART_init(&uart);
  LCD_init();
  TIMER1_setCallBack(Count_Seconds);

  /* Enable global interrupts */
  SREG |= (1 << 7);
}

/**
 * @brief Function to take the first password input from the user
 *
 * @param void
 *
 * @return void
 */
void Take_firstPassword(void) {
  /* Local variables for keypad input and loop control */
  uint8 number, i;

  /* Clear the LCD and prompt for password input */
  LCD_clearScreen();
  LCD_displayString("plz enter pass:");
  LCD_moveCursor(1, 5);

  /* Loop to read PASSWORD_SIZE digits from the keypad */
  for (i = 0; i < PASSWORD_SIZE; i++) {
    /* Get a single digit and validate it */
    number = KEYPAD_getPressedKey();
    while (number > 9) {
      number = KEYPAD_getPressedKey();
    }
    /* Store the digit and display an asterisk */
    g_firstPass[i] = number;
    LCD_displayCharacter('*');
    _delay_ms(500);
  }
}

/**
 * @brief Function to take the second password input for confirmation
 *
 * @param void
 *
 * @return void
 */
void Take_secondPassword(void) {
  /* Local variables for keypad input and loop control */
  uint8 number, i;

  /* Clear the LCD and prompt for password re-entry */
  LCD_clearScreen();
  LCD_displayString("plz re-enter the");
  LCD_displaySringRowColumn("same pass:", 1, 0);

  /* Loop to read PASSWORD_SIZE digits from the keypad */
  for (i = 0; i < PASSWORD_SIZE; i++) {
    /* Get a single digit and validate it */
    number = KEYPAD_getPressedKey();
    while (number > 9) {
      number = KEYPAD_getPressedKey();
    }
    /* Store the digit and display an asterisk */
    g_secondPass[i] = number;
    LCD_displayCharacter('*');
    _delay_ms(500);
  }
}

/**
 * @brief Function to send both entered passwords to the control ECU
 *
 * @param void
 *
 * @return void
 */
void send_Password(void) {
  /* Wait for control ECU to be ready, then send first password */
  while (UART_recieveByte() != READY_TO_RECEVIE)
    ;
  UART_sendData(g_firstPass, PASSWORD_SIZE);

  /* Wait for control ECU to be ready, then send second password */
  while (UART_recieveByte() != READY_TO_RECEVIE)
    ;
  UART_sendData(g_secondPass, PASSWORD_SIZE);
}

/**
 * @brief Function to receive a command from the control ECU
 *
 * @param void
 *
 * @return uint8
 */
uint8 receive_command(void) {
  /* Local variable to store the received command */
  uint8 response;

  /* Send ready signal and receive a command */
  UART_sendByte(READY_TO_RECEVIE);
  response = UART_recieveByte();
  return response;
}

/**
 * @brief Function to send a command to the control ECU
 *
 * @param uint8 command
 *
 * @return void
 */
void send_command(uint8 command) {
  /* Wait for control ECU to be ready, then send the command */
  while (UART_recieveByte() != READY_TO_RECEVIE)
    ;
  UART_sendByte(command);
}

/**
 * @brief Function to display the main menu and handle user selection
 *
 * @param void
 *
 * @return void
 */
void Main_Menu(void) {
  /* Local variable to store the user's menu selection */
  uint8 option;

  /* Clear the LCD and display menu options */
  LCD_clearScreen();
  LCD_displayString("+ : Open Door");
  LCD_displaySringRowColumn("- : Change Pass", 1, 0);

  /* Get the user's selection and validate it */
  option = KEYPAD_getPressedKey();
  _delay_ms(500);
  while (option != '+' && option != '-') {
    option = KEYPAD_getPressedKey();
  }

  /* Handle the selected option */
  switch (option) {
  case '+':
    Checking_Password(OPEN_DOOR);
    break;
  case '-':
    Checking_Password(CHANGING_PASSWORD);
  }
}

/**
 * @brief Function to initiate the password change process
 *
 * @param void
 *
 * @return void
 */
void Change_Password(void) { Taking_newPassword(); }

/**
 * @brief Function to handle new password entry and send it to the control ECU
 *
 * @param void
 *
 * @return void
 */
void Taking_newPassword(void) {
  /* Increment the attempt counter */
  g_attempt++;

  /* If maximum attempts reached, trigger the alarm and reset */
  if (g_attempt == 5) {
    Alarm();
    g_attempt = ZERO_ATTEMPTS;
    Take_firstPassword();
    Take_secondPassword();
    send_command(SENDING_PASSWORDS);
    send_Password();
  } else {
    /* Otherwise, take new password entries and send them */
    Take_firstPassword();
    Take_secondPassword();
    send_command(SENDING_PASSWORDS);
    send_Password();
  }
}

/**
 * @brief Function to check the entered password based on the given command
 *
 * @param uint8 command
 *
 * @return void
 */
void Checking_Password(uint8 command) {
  /* Increment the attempt counter */
  g_attempt++;

  /* If maximum attempts reached, trigger the alarm and return to main menu */
  if (g_attempt == 5) {
    Alarm();
    g_attempt = ZERO_ATTEMPTS;
    Main_Menu();
  } else {
    /* Otherwise, take the password and send the command for verification */
    Take_firstPassword();

    /* Send the appropriate command based on the action to be taken */
    switch (command) {
    case OPEN_DOOR:
      send_command(CHECKING_PASSWORD_OPEN);
      break;
    case CHANGING_PASSWORD:
      send_command(CHECKING_PASSWORD_CHANGE);
      break;
    }
    /* Wait for control ECU to be ready, then send the entered password */
    while (UART_recieveByte() != READY_TO_RECEVIE)
      ;
    UART_sendData(g_firstPass, PASSWORD_SIZE);
  }
}

/**
 * @brief Function to simulate the door opening process
 *
 * @param void
 *
 * @return void
 */
void Open_Door(void) {
  /* Clear the LCD and display the door opening message */
  LCD_clearScreen();
  LCD_displayString("OPNING THE DOOR");
  Timer1_countSeconds(FIFTEEN_SECONDS);

  /* Display the door holding message */
  LCD_clearScreen();
  LCD_displayString("HOLDING THE DOOR");
  Timer1_countSeconds(THREE_SECONDS);

  /* Display the door closing message */
  LCD_clearScreen();
  LCD_displayString("CLOSING THE DOOR");
  Timer1_countSeconds(FIFTEEN_SECONDS);
}

/**
 * @brief Function to trigger the alarm and display an error message
 *
 * @param void
 *
 * @return void
 */
void Alarm(void) {
  /* Clear the LCD and display the error message */
  LCD_clearScreen();
  LCD_displaySringRowColumn("ERROR", 0, 5);
  Timer1_countSeconds(ONE_MINUTE);
}

/**
 * @brief Callback function to count seconds using Timer1
 *
 * @param void
 *
 * @return void
 */
void Count_Seconds(void) {
  /* Increment the seconds counter */
  g_seconds++;
}

/**
 * @brief Function to count a specified number of seconds using Timer1
 *
 * @param uint8 seconds
 *
 * @return void
 */
void Timer1_countSeconds(uint8 seconds) {
  /* Timer1 configuration structure */
  TIMER1_ConfigType count_sec = {COMPARE_MODE, F_CPU_256, 0, ONE_SECOND};

  /* Initialize Timer1 with the specified configuration */
  TIMER1_init(&count_sec);

  /* Wait until the specified number of seconds has passed */
  while (g_seconds != seconds)
    ;

  /* Reset the seconds counter and deinitialize Timer1 */
  g_seconds = ZERO_SECONDS;
  TIMER1_deinit();
}
/**
 * @brief
 *
 * @param num
 *
 * @return int
 */
int call(int num) {}