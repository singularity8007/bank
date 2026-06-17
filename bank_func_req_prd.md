

# Introduction
We are trying to build a basic online bank with no intention to use actual money. However the functions and use cases will mimic functionality of actual bank. The goal of this software build is to learn large software development. Starting with simple design and adding complexity as the needs emerge. 
 ## Technology
  Operating System: Ubuntu 26.04
  Python Version:3.14+
  Database:Postgresql 18
  For web we need to use FastAPI sticking to HTTP/2. 
   We would like to implement the project with REST services for for backed processes and then the front end will be attached to it so that front end can have variety of options such as mobile(android, ios), web and we can 'sell' API to 3rd parties. 
  While this project is not a real bank and scalability and security are not prime concerns. However clean code and architecture is the prime concern due to padagogical needs. 
  No naked SQL
  No Pandas. 

 ## Double Entry Ledger
  The bank will need a Double Entry Ledger to make sure that money is **not** duplicated. For example: Person A donates 50 dollars to Person B remotely (not with cash). Person A's account must be charged -50 dollars first and then Person B will recieve 50    dollars after the first step in completed. 

 ##  Account Types
  There will be a checkings and savings account. **You can only pay for things with checking. Such as external payments.** Something like buying groceries would have to be Checking but large payments like cashier checks could be both. 

 ## Current VS Avalible Balance
   There will be two types of balances, Current and Avalible, For example: that you are sending 50 dollars to Person B, and the transaction is pending, and all the money you have is 100 dollars, your current balance would be 100 and your avalible balance  would be 50. Say that a day later, the 50 dollars went through, **Both** Current and Avalible balances would be 50.

 ## Internal Transfer
   You will be able to transfer money from Savings to Checkings, and Checkings to Savings Internally.

 ## History 
   There will be history or everything

 ## Rollbacks
   If **anything** fails, it will rollback the transaction.

# User Stories
  ## Opening an Account
  When a user wants to open an account at our bank they will be asked to fill out an oline form asking for the following information:
    
   - FirstName (Mandatory)
   - LastName (Mandatory)
   - Email (Mandatory)
   - PhoneNumber (Mandatory)
   - SocialSecurityNumber (Mandatory, Does not have to be real.)
   - DateOfBirth  (Mandatory)
   - Cust_Address (Mandatory does not have to be real)
   - Password (Mandatory, standard requirements, such as 8 char)
  On submission of the form sytem will validate customer imputs for mandatory fields and
  basic sanity checks before creating any an account entry in the system.  
## Depositing Money
  When a user wants to deposit money into their account, they will be presented with a deposit form asking for the following information:

   - Account to deposit into (Mandatory, Checking or Savings)
   - Amount (Mandatory, must be a positive number greater than zero)

On submission, the system will validate the inputs and then apply the deposit to both the Current and Available
balance of the selected account immediately, as deposits are not a pending operation.

  ## Withdrawing Money
  When a user wants to withdraw money from their account, they will be presented with a withdrawal form asking for the following information:

   - Account to withdraw from (Mandatory, Checking or Savings)
   - Amount (Mandatory, must be a positive number greater than zero)

  On submission, the system will validate that the requested amount does not exceed the Available balance of the selected account.
  If sufficient funds exist, the withdrawal is processed and both the Current and Available balances are reduced.
  If validation or processing fails at any point, the system will rollback the transaction.

  ## Transfer Money
  When a user wants to transfer money, they will be presented with a transfer form asking for the following information:

   - Transfer type (Mandatory, Internal or External)
   - Source account (Mandatory)
   - Destination account (Mandatory, for internal transfers: Checking or Savings; for external transfers: recipient account identifier)
   - Amount (Mandatory, must be a positive number greater than zero)

On submission, the system will validate that the source account has sufficient Available balance. For **internal transfers** (Savings ↔ Checking), both legs of the double-entry ledger are applied and both balances update immediately.
For **external transfers**, the debit leg is applied first, reducing the Available balance while the Current balance remains unchanged, leaving the transaction in a pending state.
Once the transfer clears, both balances are updated to reflect the final state. Only Checking accounts may be used as the source for external transfers. If any step fails, the system will rollback the entire transaction.

  ## Login
  When a user wants to log in to their account, they will be presented with a login form asking for the following information:

   - Username (Mandatory)
   - Password (Mandatory)

On submission, the system will validate that the username exists and that the provided password matches the stored credentials. If validation passes, the user is granted an authenticated session and directed to their account dashboard. If validation fails, the system will display a generic error message without specifying which field was incorrect.

  ## Log Out
  When a user wants to log out, they will select the log out option from within their session. The system will immediately invalidate the active session and redirect the user to the login page.
  No form input is required.

  ## Close Account
  When a user wants to close their account, they will be asked to confirm the following conditions before the system will proceed:

   - Account to close (Mandatory, Checking or Savings)
   - Confirmation of intent (Mandatory, explicit acknowledgment)


  ## Transaction process
    Every transaction will go through following stages:
   
    - PENDING — debit applied, credit not yet settled (external transfers only)
    - SETTLED — both legs complete
    - ROLLED_BACK — transaction failed and was reversed
    


On submission, the system will validate that the selected account has a zero balance before closing it. If the account still holds funds, the system will reject the request and prompt the user to withdraw or transfer the remaining balance first. If validation passes, the account status is updated to closed and no further transactions may be made against it. The account record is retained in the system but marked inactive.


Session behavior — note that authentication uses server-side sessions; the session token is delivered as an HTTP-only cookie. Authenticated endpoints require a valid, active session.
Audit log scope — explicitly state that the system logs all events (logins, logouts, deposits, withdrawals, transfers, account opens/closes, rollbacks) to an audit log, with outcome (success/failure).
Username clarification — state that email serves as the username. The signup form field should be labeled accordingly.
Balance columns — the PRD mentions current vs. available conceptually but never says they are stored as two discrete columns. Add one sentence making this explicit.
API-first note — add a line under Technology stating the system exposes a REST API over HTTP/2 (FastAPI) and all frontend clients consume it; no frontend-specific logic lives in the backend.

