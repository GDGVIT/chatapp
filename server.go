package main
import "github.com/kataras/iris"
import "github.com/levigross/grequests"
import "encoding/json"
type project struct {
  Name string `json:name`
  Language string `json:language`
}
type contributor struct{
  Login string `json:"login"`
  Avatar_url string `json:"avatar_url"`
}
type ProjectDetail struct {
   Name string `json:name`
   Description string `json:description`
   Contributors []contributor `json:contributor`
}
func main() {
iris.Get("/projects",ListProject)
iris.Get("/project/:project",ListProjectDetail)
iris.Listen(":8000")

}


func ListProject(ctx *iris.Context)  {
res,err:=grequests.Get("https://api.github.com/users/GDGVIT/repos",nil)
if err!=nil{
  ctx.JSON(iris.StatusOK,map[string]string{"detail":"something went wrong please contact gdg !!"})
}
var result []project
json.NewDecoder(res).Decode(&result)
ctx.JSON(iris.StatusOK,result)
}

func ListProjectDetail(ctx *iris.Context){
  res,err:=grequests.Get("https://api.github.com/repos/GDGVIT/"+ctx.Param("project"),nil)
  if err!=nil{

  }
  var result ProjectDetail
  json.NewDecoder(res).Decode(&result)
  res,err=grequests.Get("https://api.github.com/repos/GDGVIT/"+ctx.Param("project")+"/contributors",nil)
  if err!=nil{

  }
  json.NewDecoder(res).Decode(&result.Contributors)
  ctx.JSON(iris.StatusOK,result)
}
