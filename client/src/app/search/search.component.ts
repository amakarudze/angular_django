import { Component, OnInit, Input } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.css']
})
export class SearchComponent implements OnInit {
  @Input()
  passedQuery: string;
  searchQuery: string;

  constructor(private router: Router) { }

  ngOnInit() {
    console.log(this.passedQuery);
    if (this.passedQuery) {
      this.searchQuery = this.passedQuery;
    }
  }

  submitSearch(event, formData) {
    console.log(event);
    console.log(formData.value);
    let searchedQuery = formData.value['q'];
    if (searchedQuery) {
      this.router.navigate(['/search', {q: searchedQuery}]);
    // this.http.post(endpoint, {formData.value});
  }
  }
}