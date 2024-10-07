# Mosquitto MQTT Broker Setup on EC2 with SSL (Self-Signed CA)

This document provides step-by-step instructions on how to set up Mosquitto MQTT broker on an Ubuntu EC2 instance and configure it with SSL using a self-signed Certificate Authority (CA). The setup guide also explains the limitations of using a self-hosted CA.

### Prerequisites
- AWS Account with EC2 privileges.
- Basic understanding of AWS EC2 instances.
- SSH client to connect to your EC2 instance.
- Domain name (optional but recommended).

### Step 1: Launch an EC2 Instance
1. Log in to your AWS Management Console.
2. Launch an EC2 instance with the following specifications:
   - **AMI**: Ubuntu Server (preferably 20.04 LTS or later).
   - **Instance Type**: t2.micro .
   - **Security Group**: Add inbound rules to allow traffic on:
     - Port 22 (SSH)
     - Port 1883 (MQTT without SSL)
     - Port 8883 (MQTT with SSL)
3. Download the key pair (`.pem` file) for SSH access.

### Step 2: Connect to the EC2 Instance
- Connect to your instance via SSH:
  ```shell
  ssh -i "your-key.pem" ubuntu@<your-ec2-public-ip>
  ```

### Step 3: Install Mosquitto
1. Update package lists:
   ```shell
   sudo apt update
   ```
2. Install Mosquitto and Mosquitto clients:
   ```shell
   sudo apt install mosquitto mosquitto-clients -y
   ```
3. Enable Mosquitto to start on boot:
   ```shell
   sudo systemctl enable mosquitto
   ```

### Step 4: Create SSL Certificates
1. Create a directory to store SSL files:
   ```shell
   sudo mkdir -p /etc/mosquitto/certs
   cd /etc/mosquitto/certs
   ```
2. Generate a self-signed CA:
   Enter a passphrase when prompted. This secures your CA private key.
   ```shell
   sudo openssl genrsa -des3 -out ca.key 2048
   sudo openssl req -new -x509 -days 3650 -key ca.key -out ca.crt
   ```
   - Fill in the following when prompted:

    Country Name (2 letter code) [AU]: Enter your 2-letter country code (e.g., US).
    State or Province Name (full name) [Some-State]: Enter your state or province (e.g., California).
    Locality Name (eg, city) []: Enter your city (e.g., San Francisco).
    Organization Name (eg, company) [Internet Widgits Pty Ltd]: Enter your organization or company name (e.g., MyCompany Inc.).
    Organizational Unit Name (eg, section) []: (Optional) Enter your department (e.g., IT).
    Common Name (e.g., YOUR name) []: Enter a name for your CA (e.g., My MQTT CA).
    Email Address []: (Optional) Enter your email address.

3. Generate a server key and certificate signing request (CSR):
   ```shell
   sudo openssl genrsa -out server.key 2048
   sudo openssl req -new -out server.csr -key server.key
   ```
   
   Fill in the following when prompted:

    Country Name (2 letter code) [AU]: Same as before (e.g., US).
    State or Province Name (full name) [Some-State]: Same as before (e.g., California).
    Locality Name (eg, city) []: Same as before (e.g., San Francisco).
    Organization Name (eg, company) [Internet Widgits Pty Ltd]: Same as before (e.g., MyCompany Inc.).
    Organizational Unit Name (eg, section) []: (Optional) Same as before (e.g., IT).
    Common Name (e.g., YOUR name) []: Enter the public DNS or IP address of your EC2 instance. This is critical for SSL validation. Example: ec2-xx-xx-xx-xx.compute-1.amazonaws.com or your domain name if you have one.
    Email Address []: (Optional) Enter your email address.
    A challenge password []: Leave blank.
    An optional company name []: Leave blank.
    
4. Sign the server certificate with the CA:
   ```shell
   sudo openssl x509 -req -in server.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out server.crt -days 3650
   ```
   Enter the CA passphrase when prompted.

### Step 5: Configure Mosquitto for SSL
1. Edit the Mosquitto configuration file:
   ```shell
   sudo nano /etc/mosquitto/mosquitto.conf
   ```
2. Add the following configuration to enable SSL:
   ```shell
   listener 8883
   cafile /etc/mosquitto/certs/ca.crt
   certfile /etc/mosquitto/certs/server.crt
   keyfile /etc/mosquitto/certs/server.key
   require_certificate false
   allow_anonymous true
   ```
   - This configuration will enable Mosquitto to listen on port 8883 with SSL.
3. Save the file and exit (`CTRL+X`, `Y`, `Enter`).

### Step 6: Restart Mosquitto
- Restart the Mosquitto service to apply changes:
  ```shell
  sudo systemctl restart mosquitto
  ```

### Step 7: Test the MQTT Broker with SSL
1. From your local machine or another server, test using the Mosquitto client:
   ```shell
   mosquitto_pub -h <your-ec2-public-ip> -p 8883 --cafile /path/to/ca.crt -t "test/topic" -m "Hello MQTT"
   ```
2. You should be able to publish a message to the broker over SSL.


### Troubleshooting with permission
1. Adjust Permissions:
   Set the correct permissions and ownership for the certificate files:
   ```shell
   sudo chown mosquitto:mosquitto /etc/mosquitto/certs/*
   sudo chmod 644 /etc/mosquitto/certs/* 
   ```
   
### Limitations of Self-Signed SSL Certificates
1. **Trust Issues**: Self-signed certificates are not trusted by default. Clients must be explicitly configured to trust the CA.
2. **Manual Management**: You need to manually distribute the CA certificate to each client that connects.
3. **Security Risks**: Self-signed certificates do not provide identity validation, which makes it harder to ensure the server's authenticity.
4. **Scalability**: Using self-signed certificates is not practical for large-scale deployments where client trust needs to be automated.

### Additional Recommendations
- For production environments, consider using a Certificate Authority such as Let's Encrypt to generate trusted certificates.
- Make sure your EC2 security group is properly configured to allow inbound traffic only from trusted IPs.

---

## Conclusion
You have successfully set up Mosquitto on an EC2 instance with SSL encryption using a self-signed CA. This setup is suitable for testing purposes and internal applications, but for production use, consider obtaining a certificate from a trusted CA to enhance security and client trust.

---
