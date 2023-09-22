## Getting Started

### Required Software

- Java JDK (at least version 1.8)
- Ignition (at least version 7.8)
- Ignition SDK
- Maven
- Git for Windows
- KeyStore Explorer (optional)

### Environment Setup

For guidance setting up your development environment, refer to the Ignition SDK Programmer's Guide. Specifically, the following [section](https://docs.inductiveautomation.com:8443/display/SE/Environment+Setup).

Follow the steps outlined in the **How to get started** section of the **Environment Setup** documentation.

Below are a few tips from personal experience:

- Install latest Java JDK
- Download latest Maven and unzip
- Add the following "\bin" folders for Java SDK and Maven to Environment Variable "Path" (based on where each was installed):
  - C:\Program Files\Java\jdk1.8.0_112\bin
  - C:\development\apache-maven-3.3.9\bin
- Run the following from command line to set JAVA_HOME to the root of the Java SDK folder:

```shell
SET JAVA_HOME=C:\Program Files\Java\jdk1.8.0_112
```

---

## Module Signing

### Generate Java Keystore

- Switch to directory where keytool.exe is installed (JDK or JRE install location):

```shell
cd C:\Program Files\Java\jdk1.8.0_112\bin
```

- Generate keystore and create a self-signed certificate in the keystore:

```shell
keytool -genkey -keyalg RSA -alias selfsigned -keystore keystore.jks -storepass Kotter16 -validity 360 -keysize 2048
```

- Answer the prompts similar to the following:

```shell
    What is your first and last name?
      [Unknown]:  PM7510F.ecseng.com
    What is the name of your organizational unit?
      [Unknown]:  Ignition Development
    What is the name of your organization?
      [Unknown]:  ECS Solutions
    What is the name of your City or Locality?
      [Unknown]:  Evansville
    What is the name of your State or Province?
      [Unknown]:  Indiana
    What is the two-letter country code for this unit?
      [Unknown]:  US
    Is CN=PM7510F.ecseng.com, OU=Ignition Development, O=ECS Solutions, L=Evansville, ST=Indiana, C=US correct?
      [no]:  yes

    Enter key password for <selfsigned> (RETURN if same as keystore password):
```

- The "keystore.jks" file will be created in the same directory as the keytool.exe
  - Note: I moved the file to "C:\development\keystore"

### Export the self-signed certificate (*.p7b)

- Run KeyStore Explorer utility
- The following steps are based on the settings used in the command above to generate the Java Keystore:
  - Open the "keystore.jks" utility and enter the password.
  - Right-click on the "selfsigned" certificate and click "Export|Export Certificate Chain"
  - Use the following options:
    - Export Length: Entire Chain
    - Export Format: PKCS #7
    - PEM (default): True 
    - Export File (default): C:\development\keystore\selfsigned.p7b
      - Note: This path will be used below when invoking the Ignition Module Signer tool

### Self-sign Ignition Module

- Get the Ignition Module Signer tool
For guidance setting up your development environment, refer to the Ignition SDK Programmer's Guide. Specifically, the following [section](https://github.com/inductiveautomation/module-signer).

  - Switch to directory where the Ignition Module Signing Git repository should be cloned:

```shell
    cd c:\development\git
```

  - Clone the Git repository (I used Git for Windows):
  
     ```shell
     git clone https://github.com/inductiveautomation/module-signer.git
     ```

- Build the Ignition Module Signer tool using Eclipse
  - Open the *module-signer* project in your IDE from the folder you cloned the project to in the step above.
  - Clean, compile, install the project to generate the .jar file in the "target" folder of the project
- Invoke the Ignition Module Signer tool
  - Switch to the directory with the module-signer jar file:
  
```shell
    cd C:\development\git\module-signer\target
```

- Sign your module using a command similar to one shown below. Note: This is the command used to build the DVR module, you will need to change the file paths and .modl file names based on your setup.

```shell
    java ^
        -jar module-signer-1.0.0-SNAPSHOT-jar-with-dependencies.jar ^
        -keystore=C:\development\keystore\keystore.jks ^
        -keystore-pwd=Kotter16 -alias=selfsigned ^
        -alias-pwd=Kotter16 ^
        -chain=C:\development\keystore\selfsigned.p7b ^
        -module-in=C:\development\ecs-solutions\dvr-component\dvr-build\target\DVR-unsigned.modl ^
        -module-out=C:\development\ecs-solutions\dvr-component\dvr-build\target\DVR-signed.modl
```
