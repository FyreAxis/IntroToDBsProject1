using System.ComponentModel.DataAnnotations;

public class Orgs {
    [Key]
    public int OrgID {
        get;
        set;
    }
    public string? Name {
        get;
        set;
    }
    public string? Industry {
        get;
        set;
    }
    [Required]
    public int LookingForApplicants {
        get;
        set;
    }
}