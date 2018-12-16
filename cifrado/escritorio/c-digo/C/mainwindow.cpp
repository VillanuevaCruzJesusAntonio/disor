#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "cesar.hpp"
#include "inverso.hpp"
#include "inversogrupal.hpp"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow){
    ui->setupUi(this);
}

MainWindow::~MainWindow(){
    delete ui;
}

void MainWindow::on_textEntrada_modificationChanged(bool arg1){
    
    //QString textoPlano=ui->plainTextEdit_4->toPlainText();
    //b.append(cifradoCesar(ui->textEntrada->toPlainText(),ui->numSaltos->value(),abc,a));
    //buffered = cifradoCesar(ui->textEntrada->toPlainText(),ui->numSaltos->value(),abc,buffer);
    //ui->textCesar->setPlainText(buffered);
    ui->textEntrada->toPlainText();
    ui->textCesar->setPlainText(cifradoCesar(ui->textEntrada->toPlainText(),ui->numSaltos->value(),abc,a));
}
