import os
import smtplib
import imghdr
import email
import services.config

from email.message import EmailMessage

def sendReport(emailAddress, personaType):            
    msg = EmailMessage()
    msg['Subject'] = 'Your Changemaking Journey - SMU'
    msg['From'] = services.config.EMAIL_ADDRESS
    msg['To'] = emailAddress
    # msg['To'] = 'beankhin1310@gmail.com'

    # msg.set_content('This is a plain text email')


    msg.add_alternative("""\
    <!DOCTYPE html>
    <html lang="en" style="height:100%;">
    <head>
        <meta charset="utf-8" />
        <meta
        name="viewport"
        content="width=device-width, initial-scale=1, shrink-to-fit=no"
        />

    </head>
    <body>

        <div class="container">
            <br>

            <div class="container text-center">
                <h2 class="">
                    Your Changemaking Persona is CEO
                </h2>
                <br>
            </div>
            <div id="face" class="">
                <div class="row bg-light-blue" style="margin-top: -20px;">
                    <div class="col padding-0 image-choice" align="center" >
                        <img width="300px" src="https://news.smu.edu.sg/sites/news.smu.edu.sg/files/styles/max_1300x1300/public/smu/news/logoslide%2520cropped.jpg">
                    </div>
                </div>
            </div>

            <div id="personaTitle" class="container text-center">

                <div class="text-left">
                    <p>
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur aliquam enim auctor tincidunt viverra. Praesent a pretium dui. In et eros at augue mollis placerat. </p>
                    <p>Quisque eget mi venenatis, sodales risus eget, pretium tellus. Donec nec massa est. Nullam dapibus ex non rhoncus venenatis. </p>
                        Donec accumsan, augue id ultricies malesuada, urna diam faucibus odio, eget congue nibh purus sit amet orci. Morbi efficitur nibh quis vulputate lacinia. Phasellus malesuada finibus eros, sed consequat dolor. Aliquam sagittis nulla at imperdiet finibus. Curabitur vitae felis tincidunt odio tempor blandit vehicula ac dui. Nunc egestas lorem eget viverra suscipit. Phasellus nec turpis semper, tempus nunc a, maximus purus. Maecenas mattis quam eu est egestas porttitor. Vestibulum porttitor augue orci, nec aliquam dolor faucibus vitae.
                    </p>
                    <p>
                        Vestibulum sed condimentum mi. Sed egestas interdum dui sed mattis. Integer id dapibus ipsum. Vivamus laoreet sit amet tortor id commodo. Ut fringilla felis quis erat congue, posuere imperdiet tortor scelerisque. Fusce fringilla dapibus nisl, posuere faucibus tellus. Vestibulum molestie congue nisl at commodo. Nam malesuada erat eget posuere sodales.
                    </p>
                    <a href="https://lcsi.smu.edu.sg/">Learn more about Lien Center</a>
                </div>
            </div>
            
        </div>
    </body>

    </html>
    """, subtype='html')


    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(services.config.EMAIL_ADDRESS, services.config.EMAIL_PASSWORD)
        smtp.send_message(msg)
        smtp.quit()
    
    # return 200
