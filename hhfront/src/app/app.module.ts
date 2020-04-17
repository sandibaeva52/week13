import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HttpClientModule, HTTP_INTERCEPTORS} from '@angular/common/http';
import { CompaniesListComponent } from './companies-list/companies-list.component';
import { CompanyDetailComponent } from './company-detail/company-detail.component'
import {FormsModule} from "@angular/forms";
import { AuthInterceptor } from './auth.interceptor';

@NgModule({
  declarations: [
    AppComponent,
    CompaniesListComponent,
    CompanyDetailComponent

  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    AppRoutingModule,
    FormsModule
    
  ],
  providers: [
    {
    provide:HTTP_INTERCEPTORS,
    useClass:AuthInterceptor,
    multi:true
    }],
  bootstrap: [AppComponent]
})
export class AppModule { }
