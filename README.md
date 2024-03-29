# BudgetPlanner

## NOTE: The development of this project is discontinued as this repository has been archived

BudgetPlanner app for 2023 MA course; Student: Iulia-Diana Groza, Group 933/1

## Short Description

BudgetPlanner is a user-friendly mobile application available on Android & iOS, designed to help individuals manage their finances effectively. Users can easily track their income, and expenses, ensuring they stay within their budget. With a simple and intuitive interface, the app allows users to separately add, update, and remove financial entries, providing a clear overview of their financial status. Whether you're looking to save for a big purchase, or just want to get a handle on your daily spending, this app is perfect for reaching your financial goals, since it's providing statistical tools for tracking your total budget. The app supports dark mode.

-----

## Domain Details:

Income:

	ID: A unique identifier for each income entry. (Type: String)
	Amount: The amount of money associated with the entry. It must be positive. (Type: Double)
	Category: The category of the income entry, such as "Salary", "Investments", "Pension", etc. (Type: String)
	Date: The date when the income entry was made. (Type: Date)
	Note: Any additional notes or details the user wants to add about the financial entry. (Type: String)

Expense:

	ID: A unique identifier for each expenses entry. (Type: String)
	Amount: The amount of money associated with the entry. It must be positive. (Type: Double)
	Category: The category of the expenses entry, such as "Groceries", "Health", "Travel", etc. (Type: String)
	Date: The date when the expenses entry was made. (Type: Date)
	Note: Any additional notes or details the user wants to add about the financial entry. (Type: String)

-----

## CRUD Operations

Since Income and Expenses are quite similar in terms of the domain of the entity, we are presenting the CRUD operations for both of them:
* Create: Users can add a new income/expense by providing the amount, category, date, and any additional notes. A new ID is generated for each entry.
* Read: Users can view two lists, one for Savings, and one for Expenses, as well as details for a specific entry.
* Update: Users can modify the amount, category, date, and notes of an existing financial entry using its ID.
* Delete: Users can remove an existing financial entry from their associated list using its ID.

-----

## Persistence Details
* Local DB: All CRUD operations are persisted on the local database (Realm) to ensure the app remains functional even when offline. The local database is used as the primary data source.
* Server: Create, Update, and Delete operations are also persisted on a server (Firebase provided by Google) to back up user data and allow for data recovery and synchronization across devices. Read operations are typically not persisted on the server as they do not modify data.

-----

## Offline Access Scenarios

This design ensures that the Budget Planner app provides a seamless experience, even when internet connectivity is inconsistent, by relying on local data storage and synchronization.
* Create: When offline, a new financial entry is stored in the local database. It will be synchronized with the server once the device is back online.
* Read: Users can still view and search through their financial entries when offline, as this data is fetched from the local database.
* Update: Updates made while offline are saved to the local database and will be synchronized with the server once connectivity is restored.
* Delete: Entries deleted while offline are removed from the local database and this change will be reflected on the server when the device is back online.

#### © Iulia Groza
