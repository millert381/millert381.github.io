# OEE/Downtime Module - Build Notes

## Overview

The source code for the project is located in [Azure DevOps](https://dev.azure.com/ecssolutions/ECS%20MES/_git/ecs-oeedt-module).

## Make Some Changes

In the initial example, the getEquipment() function is defined under the EquipmentScriptModule class (located under 
`ecs-oeedt-common`). Let's add a simple function:

```Java    
public String doSomethingUseful() {
        return "Or not!";
}
```

That's it! We're ready to test it out! Build the module, install it, launcher the designer, open the Script Console and
 try calling the function:

```python
print system.ecs.equipment.doSomethingUseful()
```

## Building the Module

Before you can install the module on the Gateway and test it from the Script Console in the Designer, you have to build the project and sign the module. (*Technically, you could install an unsigned module, but that requires the Gateway to be running in Developer mode.*)  Below are the steps to build the module and sign it:

1. From IntelliJ, open the Maven Tool Window (View | Tool Windows | Maven).
2. Inside the Maven Tool Window, click on the **Execute Maven Goal** button or press the Ctrl key twice.
3. In the **Run Anything** window, type `clean install` and press Enter.
4. IntelliJ IDEA runs the selected goal and displays the result in the **Run** tool window.

## Sign the Module

To sign the module, we will use the **Ignition Module Signer** tool.  If you have not already done so, complete the steps outlined in the **Module Signing** section of the [How-To: Ignition Module Development](/How-To/ignition/ignition-module-development/) guide.

Once you have the tool, switch to the directory where the tool resides: 

```cmd
cd C:\development\git\module-signer\target
```

Use the command below to create a signed version of the module:

```cmd
java ^
    -jar module-signer-1.0.0-SNAPSHOT-jar-with-dependencies.jar ^
    -keystore=C:\development\keystore\keystore.jks ^
    -keystore-pwd=<password-here> -alias=selfsigned ^
    -alias-pwd=<password-here> ^
    -chain=C:\development\keystore\selfsigned.p7b ^
    -module-in=C:\Users\todd.miller\source\repos\ecs-mes\ecs-mes-build\target\ecs-mes-unsigned.modl ^
    -module-out=C:\Users\todd.miller\source\repos\ecs-mes\ecs-mes-build\target\ecs-mes.modl
```

Note the `^` character was added to allow multi-line pasting into the Windows Command Prompt.

You may need to modify the command above based on:

- Your keystore and self-signed certificate information.
- The location of your local repository.
