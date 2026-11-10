import DefaultTheme from 'vitepress/theme'
import { h } from 'vue'
import '@fontsource/noto-sans-thai/400.css'
import '@fontsource/noto-sans-thai/600.css'
import '@fontsource/noto-sans-thai/700.css'
import './custom.css'
import DayJourney from './components/DayJourney.vue'
import DownloadList from './components/DownloadList.vue'
import DownloadFile from './components/DownloadFile.vue'
import PracticeIllustration from './components/PracticeIllustration.vue'
import MarkdownWorkshopPreview from './components/MarkdownWorkshopPreview.vue'
import CourseCredits from './components/CourseCredits.vue'
export default {
  extends: DefaultTheme,
  Layout: () => h(DefaultTheme.Layout, null, { 'layout-bottom': () => h(CourseCredits) }),
  enhanceApp({ app }) {
    app.component('DayJourney', DayJourney)
    app.component('DownloadList', DownloadList)
    app.component('DownloadFile', DownloadFile)
    app.component('PracticeIllustration', PracticeIllustration)
    app.component('MarkdownWorkshopPreview', MarkdownWorkshopPreview)
  }
}
