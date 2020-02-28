import { enableProdMode } from '@angular/core';
import { platformBrowserDynamic } from '@angular/platform-browser-dynamic';

import { AppModule } from './app/app.module';
import { environment } from './environments/environment';

if (environment.production) {
  enableProdMode();
}
//calling this method is for browser-based applications. If working on different platform, you will have to use a different bootstrap method specific to that platform. You should be able to find documentation regarding how to do handle this call for that platform. 
platformBrowserDynamic().bootstrapModule(AppModule)
  .catch(err => console.error(err));
