/********************************************************************************
** Form generated from reading UI file 'NT LauncherWixlIy.ui'
**
** Created by: Qt User Interface Compiler version 5.15.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef NT_20_LAUNCHERWIXLIY_H
#define NT_20_LAUNCHERWIXLIY_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QCheckBox>
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QLabel>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QProgressBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QTextBrowser>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralwidget;
    QGroupBox *groupBox;
    QGroupBox *groupBox_2;
    QGroupBox *groupBox_6;
    QCheckBox *checkBox_debugmode;
    QCheckBox *checkBox_temploader;
    QCheckBox *checkBox_customloader;
    QLabel *label_nothingfornow;
    QGroupBox *groupBox_7;
    QPushButton *pushButton_reset;
    QPushButton *pushButton_restorefiles;
    QPushButton *pushButton_verifyfiles;
    QLabel *label_2;
    QLabel *label_3;
    QLabel *label_4;
    QLabel *label_5;
    QGroupBox *groupBox_3;
    QPushButton *pushButton_github;
    QPushButton *pushButton_updates;
    QTextBrowser *textBrowser_notablechanges;
    QGroupBox *groupBox_4;
    QPushButton *pushButton_launchstart;
    QTextBrowser *textBrowser_statuslogstart;
    QLabel *label;
    QLabel *label_note1;
    QLabel *label_note22;
    QProgressBar *progressBar;
    QGroupBox *groupBox_5;
    QLabel *label_launcherversion;
    QLabel *label_ntversion;
    QLabel *label_PTCversion;
    QLabel *label_7;
    QMenuBar *menubar;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QString::fromUtf8("MainWindow"));
        MainWindow->resize(742, 492);
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName(QString::fromUtf8("centralwidget"));
        groupBox = new QGroupBox(centralwidget);
        groupBox->setObjectName(QString::fromUtf8("groupBox"));
        groupBox->setGeometry(QRect(10, 0, 721, 431));
        groupBox_2 = new QGroupBox(groupBox);
        groupBox_2->setObjectName(QString::fromUtf8("groupBox_2"));
        groupBox_2->setGeometry(QRect(450, 20, 261, 401));
        groupBox_6 = new QGroupBox(groupBox_2);
        groupBox_6->setObjectName(QString::fromUtf8("groupBox_6"));
        groupBox_6->setGeometry(QRect(20, 20, 221, 211));
        checkBox_debugmode = new QCheckBox(groupBox_6);
        checkBox_debugmode->setObjectName(QString::fromUtf8("checkBox_debugmode"));
        checkBox_debugmode->setGeometry(QRect(10, 20, 121, 17));
        checkBox_temploader = new QCheckBox(groupBox_6);
        checkBox_temploader->setObjectName(QString::fromUtf8("checkBox_temploader"));
        checkBox_temploader->setGeometry(QRect(10, 40, 91, 17));
        checkBox_customloader = new QCheckBox(groupBox_6);
        checkBox_customloader->setObjectName(QString::fromUtf8("checkBox_customloader"));
        checkBox_customloader->setEnabled(false);
        checkBox_customloader->setGeometry(QRect(10, 60, 171, 17));
        label_nothingfornow = new QLabel(groupBox_6);
        label_nothingfornow->setObjectName(QString::fromUtf8("label_nothingfornow"));
        label_nothingfornow->setGeometry(QRect(70, 140, 151, 16));
        label_nothingfornow->setTextFormat(Qt::AutoText);
        label_nothingfornow->setScaledContents(false);
        label_nothingfornow->setWordWrap(false);
        label_nothingfornow->setTextInteractionFlags(Qt::LinksAccessibleByKeyboard|Qt::LinksAccessibleByMouse|Qt::TextBrowserInteraction|Qt::TextEditable|Qt::TextEditorInteraction|Qt::TextSelectableByKeyboard|Qt::TextSelectableByMouse);
        groupBox_7 = new QGroupBox(groupBox_2);
        groupBox_7->setObjectName(QString::fromUtf8("groupBox_7"));
        groupBox_7->setGeometry(QRect(20, 240, 221, 141));
        pushButton_reset = new QPushButton(groupBox_7);
        pushButton_reset->setObjectName(QString::fromUtf8("pushButton_reset"));
        pushButton_reset->setGeometry(QRect(10, 20, 75, 23));
        pushButton_restorefiles = new QPushButton(groupBox_7);
        pushButton_restorefiles->setObjectName(QString::fromUtf8("pushButton_restorefiles"));
        pushButton_restorefiles->setGeometry(QRect(10, 50, 75, 23));
        pushButton_verifyfiles = new QPushButton(groupBox_7);
        pushButton_verifyfiles->setObjectName(QString::fromUtf8("pushButton_verifyfiles"));
        pushButton_verifyfiles->setGeometry(QRect(10, 80, 75, 23));
        label_2 = new QLabel(groupBox_7);
        label_2->setObjectName(QString::fromUtf8("label_2"));
        label_2->setGeometry(QRect(90, 20, 171, 20));
        label_2->setLineWidth(1);
        label_2->setIndent(-1);
        label_3 = new QLabel(groupBox_7);
        label_3->setObjectName(QString::fromUtf8("label_3"));
        label_3->setGeometry(QRect(90, 50, 151, 20));
        label_4 = new QLabel(groupBox_7);
        label_4->setObjectName(QString::fromUtf8("label_4"));
        label_4->setGeometry(QRect(90, 80, 121, 20));
        label_5 = new QLabel(groupBox_7);
        label_5->setObjectName(QString::fromUtf8("label_5"));
        label_5->setGeometry(QRect(10, 100, 231, 31));
        groupBox_3 = new QGroupBox(groupBox);
        groupBox_3->setObjectName(QString::fromUtf8("groupBox_3"));
        groupBox_3->setGeometry(QRect(10, 210, 431, 161));
        pushButton_github = new QPushButton(groupBox_3);
        pushButton_github->setObjectName(QString::fromUtf8("pushButton_github"));
        pushButton_github->setGeometry(QRect(350, 130, 75, 23));
        pushButton_updates = new QPushButton(groupBox_3);
        pushButton_updates->setObjectName(QString::fromUtf8("pushButton_updates"));
        pushButton_updates->setGeometry(QRect(350, 100, 75, 23));
        textBrowser_notablechanges = new QTextBrowser(groupBox_3);
        textBrowser_notablechanges->setObjectName(QString::fromUtf8("textBrowser_notablechanges"));
        textBrowser_notablechanges->setGeometry(QRect(10, 20, 331, 131));
        groupBox_4 = new QGroupBox(groupBox);
        groupBox_4->setObjectName(QString::fromUtf8("groupBox_4"));
        groupBox_4->setGeometry(QRect(10, 20, 431, 191));
        pushButton_launchstart = new QPushButton(groupBox_4);
        pushButton_launchstart->setObjectName(QString::fromUtf8("pushButton_launchstart"));
        pushButton_launchstart->setGeometry(QRect(20, 20, 101, 23));
        textBrowser_statuslogstart = new QTextBrowser(groupBox_4);
        textBrowser_statuslogstart->setObjectName(QString::fromUtf8("textBrowser_statuslogstart"));
        textBrowser_statuslogstart->setGeometry(QRect(20, 70, 241, 111));
        label = new QLabel(groupBox_4);
        label->setObjectName(QString::fromUtf8("label"));
        label->setGeometry(QRect(20, 50, 111, 16));
        label_note1 = new QLabel(groupBox_4);
        label_note1->setObjectName(QString::fromUtf8("label_note1"));
        label_note1->setGeometry(QRect(270, 70, 171, 51));
        label_note22 = new QLabel(groupBox_4);
        label_note22->setObjectName(QString::fromUtf8("label_note22"));
        label_note22->setGeometry(QRect(270, 130, 161, 31));
        progressBar = new QProgressBar(groupBox_4);
        progressBar->setObjectName(QString::fromUtf8("progressBar"));
        progressBar->setGeometry(QRect(260, 20, 161, 23));
        progressBar->setValue(24);
        progressBar->setTextVisible(false);
        groupBox_5 = new QGroupBox(groupBox);
        groupBox_5->setObjectName(QString::fromUtf8("groupBox_5"));
        groupBox_5->setGeometry(QRect(10, 370, 431, 51));
        label_launcherversion = new QLabel(groupBox_5);
        label_launcherversion->setObjectName(QString::fromUtf8("label_launcherversion"));
        label_launcherversion->setGeometry(QRect(10, 20, 171, 16));
        label_ntversion = new QLabel(groupBox_5);
        label_ntversion->setObjectName(QString::fromUtf8("label_ntversion"));
        label_ntversion->setGeometry(QRect(200, 20, 111, 16));
        label_PTCversion = new QLabel(groupBox_5);
        label_PTCversion->setObjectName(QString::fromUtf8("label_PTCversion"));
        label_PTCversion->setGeometry(QRect(320, 20, 131, 16));
        label_7 = new QLabel(centralwidget);
        label_7->setObjectName(QString::fromUtf8("label_7"));
        label_7->setGeometry(QRect(10, 440, 631, 16));
        MainWindow->setCentralWidget(centralwidget);
        menubar = new QMenuBar(MainWindow);
        menubar->setObjectName(QString::fromUtf8("menubar"));
        menubar->setGeometry(QRect(0, 0, 742, 21));
        MainWindow->setMenuBar(menubar);
        statusbar = new QStatusBar(MainWindow);
        statusbar->setObjectName(QString::fromUtf8("statusbar"));
        MainWindow->setStatusBar(statusbar);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QCoreApplication::translate("MainWindow", "NT Launcher 1.0", nullptr));
#if QT_CONFIG(whatsthis)
        MainWindow->setWhatsThis(QString());
#endif // QT_CONFIG(whatsthis)
        MainWindow->setWindowFilePath(QString());
        groupBox->setTitle(QCoreApplication::translate("MainWindow", "Launcher", nullptr));
        groupBox_2->setTitle(QCoreApplication::translate("MainWindow", "Settings", nullptr));
        groupBox_6->setTitle(QCoreApplication::translate("MainWindow", "NT ", nullptr));
        checkBox_debugmode->setText(QCoreApplication::translate("MainWindow", "Debug Mode", nullptr));
        checkBox_temploader->setText(QCoreApplication::translate("MainWindow", "Temp Loader", nullptr));
        checkBox_customloader->setText(QCoreApplication::translate("MainWindow", "Load Custom Extensions", nullptr));
        label_nothingfornow->setText(QCoreApplication::translate("MainWindow", "Nohting For Now", nullptr));
        groupBox_7->setTitle(QCoreApplication::translate("MainWindow", "System", nullptr));
        pushButton_reset->setText(QCoreApplication::translate("MainWindow", "Reset", nullptr));
        pushButton_restorefiles->setText(QCoreApplication::translate("MainWindow", "Restore Files", nullptr));
        pushButton_verifyfiles->setText(QCoreApplication::translate("MainWindow", "Verify Files", nullptr));
        label_2->setText(QCoreApplication::translate("MainWindow", "Will Reset Everything", nullptr));
        label_3->setText(QCoreApplication::translate("MainWindow", "Restore The Missing Files", nullptr));
        label_4->setText(QCoreApplication::translate("MainWindow", "Verify Files.", nullptr));
        label_5->setText(QCoreApplication::translate("MainWindow", "NOTE: Watch The \"Status Log\" To Be \n"
"Informed About The Prcoess.", nullptr));
        groupBox_3->setTitle(QCoreApplication::translate("MainWindow", "NotAbleChanges", nullptr));
        pushButton_github->setText(QCoreApplication::translate("MainWindow", "Github", nullptr));
        pushButton_updates->setText(QCoreApplication::translate("MainWindow", "Updates", nullptr));
        groupBox_4->setTitle(QCoreApplication::translate("MainWindow", "Start", nullptr));
        pushButton_launchstart->setText(QCoreApplication::translate("MainWindow", "Launch NT 1.0", nullptr));
        textBrowser_statuslogstart->setHtml(QCoreApplication::translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", nullptr));
        label->setText(QCoreApplication::translate("MainWindow", "Status Log :", nullptr));
        label_note1->setText(QCoreApplication::translate("MainWindow", "NOTE: Some Settings Wont Be\n"
" Applied In Action Until You \n"
"Restart NT Or Faced \n"
"A Force Boot Side.", nullptr));
        label_note22->setText(QCoreApplication::translate("MainWindow", "NOTE: The Debug Mode May \n"
"Cost Some Bugs And Hanging.", nullptr));
        groupBox_5->setTitle(QCoreApplication::translate("MainWindow", "Information", nullptr));
        label_launcherversion->setText(QCoreApplication::translate("MainWindow", "Launcher Version :", nullptr));
        label_ntversion->setText(QCoreApplication::translate("MainWindow", "NT Version :", nullptr));
        label_PTCversion->setText(QCoreApplication::translate("MainWindow", "PTC Version : 1.7.54", nullptr));
        label_7->setText(QCoreApplication::translate("MainWindow", "Author : suegdu | suegdu Github. do not disturb!.  NT Are Licensed Under The Creative Commons Zero v1.0 Universal License.", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // NT_20_LAUNCHERWIXLIY_H
